#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
state_dir="${NKPT_TEX_STATE_DIR:-$(dirname "$repo_dir")}"
if [[ "$state_dir" != /* ]]; then
    echo "NKPT_TEX_STATE_DIR must be an absolute path." >&2
    exit 2
fi
tex_root="$state_dir/.texlive-extra"
apt_root="$state_dir/.book-apt"

for command in python3 kpsewhich latexmk pdflatex bibtex makeindex pdfinfo pdftotext; do
    if ! command -v "$command" >/dev/null 2>&1; then
        echo "Missing $command. Install the base TeX Live, latexmk, Python, and Poppler tools described in README.md." >&2
        exit 1
    fi
done

source "$repo_dir/scripts/tex-env.sh"
required_files=(newtxtext.sty newtxmath.sty dsfont.sty binhex.tex ot1qhv.fd)
missing=0
for file in "${required_files[@]}"; do
    if ! kpsewhich "$file" >/dev/null; then
        missing=1
    fi
done

if (( missing )); then
    if [[ ! -r /etc/os-release ]]; then
        echo "Missing TeX packages; install newtx, doublestroke, and TeX Gyre using your TeX distribution." >&2
        exit 1
    fi
    source /etc/os-release
    if [[ "${ID:-}" != debian || "${VERSION_CODENAME:-}" != trixie ]]; then
        echo "Automatic package download requires Debian 13 (trixie). Install newtx, doublestroke, and TeX Gyre using your TeX distribution." >&2
        exit 1
    fi
    for command in apt-get dpkg-deb; do
        command -v "$command" >/dev/null 2>&1 || { echo "Missing $command." >&2; exit 1; }
    done
    mkdir -p "$apt_root/lists/partial" "$apt_root/cache/archives/partial" "$tex_root"
    printf '%s\n' 'deb [signed-by=/usr/share/keyrings/debian-archive-keyring.gpg] https://deb.debian.org/debian trixie main' > "$apt_root/sources.list"
    apt_options=(
        -o "Dir::State::lists=$apt_root/lists"
        -o "Dir::Cache=$apt_root/cache"
        -o "Dir::Etc::sourcelist=$apt_root/sources.list"
        -o Dir::Etc::sourceparts=-
        -o Debug::NoLocking=1
    )
    apt-get "${apt_options[@]}" update
    (
        cd "$apt_root"
        apt-get "${apt_options[@]}" download \
            texlive-fonts-extra=2024.20250309-2 \
            texlive-plain-generic=2024.20250309-2 \
            tex-gyre=20180621-6
    )
    dpkg-deb -x "$apt_root/texlive-fonts-extra_2024.20250309-2_all.deb" "$tex_root"
    dpkg-deb -x "$apt_root/texlive-plain-generic_2024.20250309-2_all.deb" "$tex_root"
    dpkg-deb -x "$apt_root/tex-gyre_20180621-6_all.deb" "$tex_root"
    rm -f "$apt_root/texlive-fonts-extra_2024.20250309-2_all.deb" \
          "$apt_root/texlive-plain-generic_2024.20250309-2_all.deb" \
          "$apt_root/tex-gyre_20180621-6_all.deb"
    source "$repo_dir/scripts/tex-env.sh"
fi

if [[ -f "$tex_root/usr/share/texlive/texmf-dist/fonts/map/dvips/newtx/newtx.map" ]]; then
    updmap-user --enable Map=newtx.map --enable Map=dstroke.map --enable Map=qhv.map
fi
for file in "${required_files[@]}"; do
    kpsewhich "$file" >/dev/null || { echo "TeX package still unavailable: $file" >&2; exit 1; }
done
echo "TeX dependencies ready. In each new shell, run: source scripts/tex-env.sh"
