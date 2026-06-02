# Stephanie Stewart — Design Portfolio

A single-page portfolio of selected graphic design work for two nonprofit partners:
Duquesne University and Ronald McDonald House Charities (Pittsburgh & Morgantown).

## Run locally

No build step or dependencies. Either open `index.html` directly in a browser, or serve it:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Features

- **Two themes** — toggle between a minimal gallery look and a bold/branded look (top-right switch).
- **Lightbox** — click any piece to view it larger; multi-page pieces step through with arrow keys.
- **Responsive** — adapts from desktop to mobile.

## Structure

- `index.html` — the entire site (HTML, CSS, JS inline).
- `assets/` — web-optimized JPG previews of each piece.
