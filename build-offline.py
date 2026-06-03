#!/usr/bin/env python3
"""Build a single self-contained offline HTML file.

Reads index.html, inlines every image in assets/ as a base64 data URI, and
writes "Stephanie Stewart Portfolio (offline).html" — one file that works in
any browser with no internet and no separate assets folder.

Re-run this after editing index.html or changing any images:
    python3 build-offline.py
"""
import re, base64, os, mimetypes

SRC = "index.html"
OUT = "Stephanie Stewart Portfolio (offline).html"


def datauri(path):
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    data = base64.b64encode(open(path, "rb").read()).decode("ascii")
    return f"data:{mime};base64,{data}"


def main():
    html = open(SRC, "r", encoding="utf-8").read()
    refs = sorted(set(re.findall(r"assets/[A-Za-z0-9._-]+", html)))
    missing = [r for r in refs if not os.path.exists(r)]
    if missing:
        raise SystemExit(f"Missing assets, aborting: {missing}")
    # Replace longest first so shorter names can't partial-match inside longer ones.
    for ref in sorted(refs, key=len, reverse=True):
        html = html.replace(ref, datauri(ref))
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)/1e6:.1f} MB) from {len(refs)} images.")


if __name__ == "__main__":
    main()
