#!/usr/bin/env bash
# Source this file in each shell before building from a local TeX installation.

_nkpt_repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
_nkpt_state_dir="${NKPT_TEX_STATE_DIR:-$(dirname "$_nkpt_repo_dir")}"
_nkpt_tex_root="$_nkpt_state_dir/.texlive-extra"
_nkpt_tex_dist="$_nkpt_tex_root/usr/share/texlive/texmf-dist"
_nkpt_tex_gyre="$_nkpt_tex_root/usr/share/texmf"

if [[ -d "$_nkpt_tex_dist" || -d "$_nkpt_tex_gyre" ]]; then
    for _nkpt_path in "$_nkpt_tex_dist" "$_nkpt_tex_gyre"; do
        if [[ -d "$_nkpt_path" && ":${TEXMFHOME:-}:" != *":$_nkpt_path:"* ]]; then
            TEXMFHOME="$_nkpt_path${TEXMFHOME:+:$TEXMFHOME}"
        fi
    done
    export TEXMFHOME
    export TEXMFVAR="$_nkpt_state_dir/.texlive-var"
    export TEXMFCONFIG="$_nkpt_state_dir/.texlive-config"
fi

unset _nkpt_repo_dir _nkpt_state_dir _nkpt_tex_root _nkpt_tex_dist _nkpt_tex_gyre _nkpt_path
