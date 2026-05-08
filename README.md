# sharky

**sharky** is a YAML-driven static site generator.  
You edit YAML files in `content/`, then run Python to build a ready-to-serve site in `dist/`.

## Quick start

```bash
git clone https://github.com/ttiramisu/sharky.git
cd sharky
pip install -r requirements.txt
python3 dev.py
```

Open `http://localhost:6767`.

To build once (no dev server):

```bash
python3 main.py
```

## How it works

1. Configure site metadata in `content/CONFIG.yaml`.
2. Configure navbar/footer links in `content/NAVIGATION.yaml`.
3. Define one or more pages in `content/CONFIG.yaml` (`pages` list).
4. Build output goes to:
   - `dist/*.html` (one file per configured page)
   - `dist/web/*` (copied assets and CSS)

## Project layout

```text
sharky/
├─ content/              # YAML input files
├─ web/                  # source assets (images, css)
├─ engine/               # HTML generation logic
├─ scripts/              # build + dev server entrypoints
├─ dist/                 # generated output
├─ main.py               # build wrapper
└─ dev.py                # dev server wrapper
```

## YAML files

### `content/CONFIG.yaml`

Global site config:

```yaml
language: en
website-name: My Site
website-icon: web/assets/icon.jpg
description: Short description for SEO
custom_css: web/css/style.css
pages:
  - output: index.html
    title: My Site - Home
    content: CONTENTS.yaml
  - output: about.html
    title: My Site - About
    content: pages/about.yaml
    navigation: NAVIGATION.yaml
```

If `pages` is omitted, Sharky falls back to single-page mode using `content/CONTENTS.yaml`.

### `content/NAVIGATION.yaml`

Navbar title/logo and navigation links:

```yaml
nav_title: My Site
logo: web/assets/icon.jpg
items:
  - label: Home
    href: index.html
  - label: Features
    href: index.html#features
  - label: Contact
    href: contact.html
```

Use `href` for page links (e.g. `about.html`) and `id` for same-page anchors (e.g. `#features`).

### `content/CONTENTS.yaml`

Defines page blocks in render order.
Each list item uses a consistent shape with a required `block` field plus block-specific keys.
For multi-page sites, add additional files under `content/pages/*.yaml` and reference them from `pages` in `CONFIG.yaml`.

Supported block types:

| Block | Purpose |
| --- | --- |
| `hero` | Hero section with title/text/image/buttons |
| `two-col` | Two-column text + image layout |
| `text_row` | Row of text items |
| `img_row` | Row of image items |
| `carousel` | Image carousel |
| `jumbo` | Large emphasis section |
| `stats` | KPI/stat cards in a row |
| `quote` | Centered quote/testimonial |
| `cta` | Call-to-action section with button |
| `divider` | Horizontal section divider |
| `spacing` | Vertical space (pixels) |
| `scroll_to` | Anchor target for navigation/buttons |

## Content examples

### Hero

```yaml
- block: hero
  type: centered_hero
  img: web/assets/icon.jpg
  img_width: 600
  img_height: 320
  title: Welcome
  text: Intro text here
  btn_primary: Learn more
  btn_secondary:
  btn_primary_id: features
  btn_secondary_id:
```

Hero `type` options:
- `centered_hero`
- `centered_screenshot`
- `text_left_img_right`
- `border_crop_img`

### Two-column section

```yaml
- block: two-col
  class: ''
  title: About us
  text: Section body text
  img: web/assets/icon.jpg
  img_position: left
```

`img_position` can be `left` or `right`.

### Text row

```yaml
- block: text_row
  class: ''
  items:
    - One
    - Two
    - Three
```

### Image row

```yaml
- block: img_row
  class: ''
  items:
    - web/assets/icon.jpg
    - web/assets/icon.jpg
```

### Carousel

```yaml
- block: carousel
  content:
    - web/assets/icon.jpg
    - web/assets/icon.jpg
  width: 800
  height: 400
```

### Jumbo

```yaml
- block: jumbo
  type: basic
  title: Big message
  text: Supporting text
```

Jumbo `type` options:
- `basic`
- `full_width`

### Stats

```yaml
- block: stats
  items:
    - value: 120K+
      label: Users
    - value: 48
      label: Teams
    - value: 99.9%
      label: Uptime
```

### Quote

```yaml
- block: quote
  text: |
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  author: Jane Doe
```

### CTA

```yaml
- block: cta
  title: Start now
  text: |
    Lorem ipsum dolor sit amet.
  button: Contact us
  href: contact.html
```

### Divider

```yaml
- block: divider
```

### Spacing and scroll target

```yaml
- block: spacing
  value: 50

- block: scroll_to
  id: features
```

## Notes

- If a hero button text is empty, that button is omitted.
- Paths in YAML should point to files under `web/`.
- `dev.py` auto-rebuilds when YAML/CSS changes.
- Build now performs basic validation for missing files and invalid YAML shapes.

## License

MIT. See `LICENSE`.
