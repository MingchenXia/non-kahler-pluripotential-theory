#!/usr/bin/env python3
"""Commit curated manuscript changes and verify a push to the private repository."""
import argparse
import fcntl
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
REPO = "MingchenXia/non-kahler-pluripotential-theory"
REMOTE = f"https://github.com/{REPO}.git"
PATHS = [".gitignore", ".gitattributes", "AGENTS.md", "README.md", "PLAN.md",
         "BLUEPRINT.md", "CHANGELOG.md", "book", "research", "scripts"]
SECRET = re.compile(
    rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----|"
    rb"\bgh[pousr]_[A-Za-z0-9]{30,}\b|"
    rb"\bgithub_pat_[A-Za-z0-9_]{40,}\b|"
    rb"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{32,}\b"
)


def run(*args, capture=True):
    return subprocess.run(args, cwd=ROOT, check=True,
                          stdout=subprocess.PIPE if capture else None,
                          text=True).stdout


def synchronize(message):
    if run("git", "branch", "--show-current").strip() != "main":
        raise RuntimeError("Expected branch main; no changes were staged.")
    if run("git", "remote", "get-url", "origin").strip() != REMOTE:
        raise RuntimeError("Unexpected origin; no changes were staged.")
    # Check before committing or sending any repository content.
    info = json.loads(run("gh", "api", f"repos/{REPO}", "--jq",
                          "{nameWithOwner: .full_name, visibility: .visibility, private: .private}"))
    if (info.get("nameWithOwner") != REPO
            or info.get("visibility") != "private"
            or info.get("private") is not True):
        raise RuntimeError("The expected repository must be private.")
    git_dir = Path(run("git", "rev-parse", "--absolute-git-dir").strip())
    if any((git_dir / p).exists() for p in
           ["MERGE_HEAD", "CHERRY_PICK_HEAD", "rebase-merge", "rebase-apply"]):
        raise RuntimeError("Finish the existing Git operation before synchronizing.")
    if run("git", "ls-files", "-u").strip():
        raise RuntimeError("Unresolved conflicts; local files were preserved.")

    run("git", "fetch", "origin")
    # An absent remote main is expected for the first push only.
    local = subprocess.run(["git", "rev-parse", "--verify", "HEAD"],
                           cwd=ROOT, capture_output=True, text=True)
    remote = subprocess.run(["git", "rev-parse", "--verify", "origin/main"],
                            cwd=ROOT, capture_output=True, text=True)
    if remote.returncode == 0:
        if local.returncode != 0 or subprocess.run(
            ["git", "merge-base", "--is-ancestor", "origin/main", "HEAD"],
            cwd=ROOT, capture_output=True).returncode != 0:
            raise RuntimeError("Remote main has changes to reconcile; no force push.")

    # Include new files as well as modifications and deletions, respecting ignores.
    candidates = run("git", "ls-files", "--cached", "--others",
                     "--exclude-standard", "-z").split("\0")
    for name in filter(None, candidates):
        if name.split("/", 1)[0] not in PATHS:
            raise RuntimeError(f"Unexpected source path: {name}")
        path = ROOT / name
        if path.is_symlink():
            raise RuntimeError(f"Review symlink before synchronization: {name}")
        if path.is_file():
            if path.stat().st_size > 10 * 1024 * 1024:
                raise RuntimeError(f"Review large file before synchronization: {name}")
            if SECRET.search(path.read_bytes()):
                raise RuntimeError(f"Possible credential in {name}; nothing staged.")

    run("git", "add", "-A", "--", *PATHS)
    changed = run("git", "diff", "--cached", "--name-only").strip()
    if changed:
        # Preserve supplied template files and immutable verifier output verbatim.
        run("git", "diff", "--cached", "--check", "--", ".",
            ":(exclude)book/style/**", ":(exclude)research/rethlas/verification/**")
        run("git", "commit", "-m", message, capture=False)
    elif local.returncode != 0:
        raise RuntimeError("No curated files to commit.")
    run("git", "push", "--set-upstream", "origin", "main", capture=False)
    head = run("git", "rev-parse", "HEAD").strip()
    remote_head = run("git", "ls-remote", "origin", "refs/heads/main").split()[0]
    if head != remote_head:
        raise RuntimeError("Remote head differs; inspect before reporting success.")
    print(f"Verified private GitHub backup: {REPO}@{head}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--message", required=True, help="Substantive commit summary")
    args = parser.parse_args()
    if not args.message.strip():
        parser.error("Provide a nonempty commit summary.")
    git_dir = Path(run("git", "rev-parse", "--absolute-git-dir").strip())
    with (git_dir / "manuscript-sync.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        synchronize(args.message)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError, BlockingIOError) as error:
        print(f"Synchronization stopped: {error}", file=sys.stderr)
        sys.exit(1)
