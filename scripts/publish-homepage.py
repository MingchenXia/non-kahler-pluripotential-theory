#!/usr/bin/env python3
"""Publish this book's PDF and matching homepage description in one commit."""
import argparse
import base64
import datetime
import fcntl
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SOURCE_REMOTE = "https://github.com/MingchenXia/non-kahler-pluripotential-theory.git"
SITE_REPO = "MingchenXia/mingchenxia.github.io"
BRANCH = "main"
PDF_PATH = "Papers/SHPT_vibe.pdf"
PAGE_PATH = "readme.md"
BOOK_LINK = "[Singularities in Hermitian pluripotential theory](Papers/SHPT_vibe.pdf)"


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def is_authoring_checkout():
    try:
        top = Path(run("git", "-C", str(ROOT), "rev-parse", "--show-toplevel").strip())
        remote = run("git", "-C", str(ROOT), "remote", "get-url", "origin").strip()
        return top.resolve() == ROOT and remote == SOURCE_REMOTE
    except subprocess.CalledProcessError:
        return False


def index_page_number(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return None
    # The book ends with its index. Read the printed running head, never PDF length.
    m = re.fullmatch(r"(?:Index\s+([1-9][0-9]*)|([1-9][0-9]*)\s+Index)", lines[0])
    if not m:
        raise RuntimeError("Cannot identify the final printed index page; inspect the PDF.")
    return int(m.group(1) or m.group(2))


def printed_page_number(pdf):
    info = run("pdfinfo", str(pdf))
    m = re.search(r"^Pages:\s+(\d+)\s*$", info, re.M)
    if not m:
        raise RuntimeError("Cannot read the PDF structure.")
    total = int(m.group(1))
    for physical in range(total, max(0, total - 8), -1):
        text = run("pdftotext", "-f", str(physical), "-l", str(physical), "-layout", str(pdf), "-")
        printed = index_page_number(text)
        if printed is not None:
            return printed, total, physical
    raise RuntimeError("No printed page number in the last eight PDF pages.")


def update_abstract(source, pages, date):
    if source.count(BOOK_LINK) != 1:
        raise RuntimeError("Expected exactly one homepage entry for this book.")
    start = source.index(BOOK_LINK) + len(BOOK_LINK)
    end = source.find("\n- ", start)
    if end == -1:
        end = len(source)
    section = source[start:end]
    pattern = r"(> \*\*Abstract\.\*\* )A research monograph\. [0-9]+ pages\. Updated [A-Za-z]+ [0-9]{1,2}, [0-9]{4}\."
    description = f"A research monograph. {pages} pages. Updated {date}."
    section, count = re.subn(pattern, lambda m: m.group(1) + description, section)
    if count != 1:
        raise RuntimeError("The book's abstract has changed; inspect it before publishing.")
    return source[:start] + section + source[end:], description


def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def api(endpoint, method="GET", payload=None):
    cmd = ["gh", "api", f"repos/{SITE_REPO}/{endpoint}", "--method", method]
    if payload is not None:
        cmd += ["--input", "-"]
    result = subprocess.run(cmd, input=json.dumps(payload) if payload is not None else None,
                            capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def tree_entries(tree_sha):
    response = api(f"git/trees/{tree_sha}?recursive=1")
    if response.get("truncated"):
        raise RuntimeError("Incomplete website tree; no publication attempted.")
    return {entry["path"]: entry for entry in response["tree"] if entry["type"] == "blob"}


def publish(dry_run):
    pdf = ROOT / "output/pdf/hermitian-pluripotential-theory.pdf"
    data = pdf.read_bytes()
    if data != (ROOT / "book/book.pdf").read_bytes():
        raise RuntimeError("The delivery PDF differs from the current book build.")
    log = (ROOT / "book/book.log").read_text(encoding="latin1")
    if re.search(r"(^!|undefined|multiply defined|Overfull)", log, re.M):
        raise RuntimeError("Resolve the book build diagnostics before publication.")
    pages, physical_pages, numbered_physical_page = printed_page_number(pdf)
    today = datetime.date.today()
    date = f"{today.strftime('%B')} {today.day}, {today.year}"
    head = api(f"git/ref/heads/{BRANCH}")["object"]["sha"]
    parent = api(f"git/commits/{head}")
    original = tree_entries(parent["tree"]["sha"])
    for name in [PDF_PATH, PAGE_PATH]:
        if name not in original or original[name]["mode"] != "100644":
            raise RuntimeError(f"Unexpected website target: {name}")
    readme_blob = api(f"git/blobs/{original[PAGE_PATH]['sha']}")
    if readme_blob["encoding"] != "base64":
        raise RuntimeError("Unexpected homepage encoding.")
    readme = base64.b64decode(readme_blob["content"]).decode("utf-8")
    updated, description = update_abstract(readme, pages, date)
    payloads = {PDF_PATH: data, PAGE_PATH: updated.encode("utf-8")}
    changed = {name: value for name, value in payloads.items()
               if blob_sha(value) != original[name]["sha"]}
    report = {"repository": SITE_REPO, "branch": BRANCH, "parent": head,
              "printed_last_page": pages, "physical_pdf_pages": physical_pages,
              "numbered_physical_page": numbered_physical_page, "description": description,
              "pdf_sha256": hashlib.sha256(data).hexdigest(), "changed_paths": list(changed),
              "date": today.isoformat(), "dry_run": dry_run}
    if dry_run:
        print(json.dumps(report, indent=2))
        return
    if changed:
        entries = []
        for name, value in changed.items():
            blob = api("git/blobs", "POST", {"content": base64.b64encode(value).decode(), "encoding": "base64"})
            if blob["sha"] != blob_sha(value):
                raise RuntimeError("Uploaded blob checksum differs.")
            entries.append({"path": name, "mode": "100644", "type": "blob", "sha": blob["sha"]})
        tree = api("git/trees", "POST", {"base_tree": parent["tree"]["sha"], "tree": entries})
        resulting = tree_entries(tree["sha"])
        differences = {p for p in original.keys() | resulting.keys() if original.get(p) != resulting.get(p)}
        if differences != set(changed):
            raise RuntimeError("Website tree changes exceed the two authorized files.")
        commit = api("git/commits", "POST", {
            "message": f"Update Hermitian pluripotential monograph ({pages} pages, {date})",
            "tree": tree["sha"], "parents": [head]})
        # A concurrent website update must be retained, never force-pushed over.
        api(f"git/refs/heads/{BRANCH}", "PATCH", {"sha": commit["sha"], "force": False})
        head = commit["sha"]
    live_head = api(f"git/ref/heads/{BRANCH}")["object"]["sha"]
    live_tree = tree_entries(api(f"git/commits/{live_head}")["tree"]["sha"])
    if any(live_tree[name]["sha"] != blob_sha(value) for name, value in payloads.items()):
        raise RuntimeError("Remote files differ after publication; inspect concurrent changes.")
    report.update(commit=head, verified_remote_head=live_head, remote_files_verified=True)
    out = ROOT / "output/publication"
    out.mkdir(parents=True, exist_ok=True)
    (out / "latest.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Homepage repository updated: {description}\nVerified commit: {live_head}")
    print("GitHub Pages deployment is asynchronous; verify the public PDF and homepage after deployment.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from-build", action="store_true", help="Skip publication for extracted source packages.")
    parser.add_argument("--dry-run", action="store_true", help="Read and preview; do not change the website.")
    args = parser.parse_args()
    if not is_authoring_checkout():
        if args.from_build:
            print("Source-package build: homepage publication is not enabled outside the authoring repository.")
            return
        raise RuntimeError("Run publication from the authorized book repository.")
    out = ROOT / "output/publication"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "publish.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        publish(args.dry_run)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print(f"Homepage publication stopped: {error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr.strip(), file=sys.stderr)
        sys.exit(1)
