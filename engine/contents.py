'''
utils/contents.py

This module provides the function to read the CONTENTS.yaml file and process them into actual html
'''

import yaml
from collections import defaultdict
from pathlib import Path
import re
import sys

# CUSTOM COMPONENTS
from engine.components.row import row
from engine.components.two_col import two_col_img_left as two_col_left
from engine.components.two_col import two_col_img_right as two_col_right
from engine.helper.mb import mb as mb
from engine.helper.scrollto import scroll_to_id as st_id

# HERO COMPONENTS
from engine.components.hero import centered_hero, centered_screenshot, text_left_img_right, border_crop_img

# JUMBOTRON COMPONENTS
from engine.components.jumbo import basic, full_width

# CAROUSEL COMPONENTS
from engine.components.carousel import carousel, first_frame, other_frame
from engine.components.extras import cta_block, divider_block, quote_block, stats_block, stats_item

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENTS_PATH = PROJECT_ROOT / "content" / "CONTENTS.yaml"


def load_contents(contents_path=None):
    file_path = Path(contents_path) if contents_path else CONTENTS_PATH
    if not file_path.is_absolute():
        file_path = PROJECT_ROOT / file_path
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file) or []
    except FileNotFoundError as err:
        raise RuntimeError(f"Content file not found: {file_path}") from err
    except yaml.YAMLError as err:
        raise RuntimeError(f"Invalid YAML in content file: {file_path}") from err


def _flatten_mapping(value):
    if isinstance(value, dict):
        return value

    flattened = {}
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                flattened.update(item)
    return flattened


def normalize_block(raw_block):
    """
    Normalize CONTENTS.yaml blocks to a single schema:
    - block: <type>
    - remaining keys: block payload
    """

    if not isinstance(raw_block, dict):
        return None

    if "block" in raw_block:
        normalized = dict(raw_block)
        normalized["block"] = str(normalized["block"])
        return normalized

    block_keys = (
        "hero",
        "jumbo",
        "two-col",
        "text_row",
        "img_row",
        "carousel",
        "spacing",
        "scroll_to",
        "quote",
        "cta",
        "stats",
        "divider",
    )
    for key in block_keys:
        if key not in raw_block:
            continue
        if key in ("spacing", "scroll_to"):
            return {"block": key, "value": raw_block[key]}
        return {"block": key, **_flatten_mapping(raw_block[key])}

    return None


def hero_maker(hero_data):
    """
    Takes a hero block from YAML and routes it to the correct hero component.
    Buttons with empty text are removed entirely.
    Images with no value are also removed.
    """

    hero_type = hero_data.get("type", "").lower()

    hero_map = {
        "centered_hero": centered_hero,
        "centered_screenshot": centered_screenshot,
        "text_left_img_right": text_left_img_right,
        "border_crop_img": border_crop_img
    }

    if hero_type not in hero_map:
        return f"<!-- Unknown hero type: {hero_type} -->"

    # Work on a copy of the template
    hero_html = hero_map[hero_type]

    # Remove <img> tags if the image data is empty
    for img in ["primary", "secondary"]:
        img_key = f"img_{img}"
        img_id_key = f"img_{img}_id"
        if not hero_data.get(img_key):
            pattern = rf'<img[^>]*{img_id_key}[^>]*>'
            hero_html = re.sub(pattern, '', hero_html, flags=re.DOTALL)

    # Remove buttons entirely if text is empty
    for btn in ["primary", "secondary"]:
        btn_key = f"btn_{btn}"
        btn_id_key = f"btn_{btn}_id"
        if not hero_data.get(btn_key):
            pattern = rf'<a[^>]*{btn_id_key}[^>]*>.*?</a>'
            hero_html = re.sub(pattern, '', hero_html, flags=re.DOTALL)

    # Format remaining placeholders safely
    return hero_html.format_map(defaultdict(str, hero_data))


def jumbotron_maker(block):
    """
    Takes a jumbotron block from YAML and generates the HTML
    based on its type.
    """

    jumbotron_map = {
        "basic": basic,
        "full_width": full_width,
    }

    jumbo_type = block.get("type", "basic").lower()
    jumbotron_html = jumbotron_map.get(jumbo_type)

    if not jumbotron_html:
        return f"<!-- Unknown jumbotron type: {jumbo_type} -->"

    return jumbotron_html.format_map(defaultdict(str, block))


def render_error(block_type, message):
    print(f"[content] {block_type}: {message}", file=sys.stderr)
    return f"<!-- {block_type} error: {message} -->"


def required(block, block_type, fields):
    missing = [field for field in fields if not block.get(field)]
    if missing:
        return render_error(block_type, f"missing required fields: {', '.join(missing)}")
    return None


def quote_maker(block):
    validation = required(block, "quote", ["text"])
    if validation:
        return validation
    author = block.get("author", "Anonymous")
    return quote_block.format_map(defaultdict(str, {"text": block.get("text", ""), "author": author}))


def cta_maker(block):
    validation = required(block, "cta", ["title", "text", "button", "href"])
    if validation:
        return validation
    return cta_block.format_map(defaultdict(str, block))


def stats_maker(block):
    items = block.get("items", [])
    if not isinstance(items, list) or not items:
        return render_error("stats", "items must be a non-empty list")

    html_items = []
    for item in items:
        if not isinstance(item, dict):
            return render_error("stats", "each item must be a map with value and label")
        if not item.get("value") or not item.get("label"):
            return render_error("stats", "each item must include value and label")
        html_items.append(stats_item.format_map(defaultdict(str, item)))

    return stats_block.format(items="".join(html_items))

def make_final_content(contents_path=None):
    """
    Makes the content html in order of the CONTENTS.yaml file
    """

    final_content = ''
    contents = load_contents(contents_path)
    if not isinstance(contents, list):
        raise RuntimeError(f"Expected a list of blocks in {contents_path or CONTENTS_PATH}")

    for raw_block in contents:
        block = normalize_block(raw_block)
        if not block:
            final_content += render_error("block", "invalid block shape")
            continue

        block_type = block.get("block")

        if block_type == "text_row":
            cls = block.get('class', '')
            items = block.get('items', [])

            row_items = "".join(
                f'<div class="col {cls}">{item}</div>' for item in items)
            final_content += row.format(row_items=row_items)

        elif block_type == "img_row":
            cls = block.get('class', '')
            items = block.get('items', [])

            row_items = "".join(
                f'<div class="col {cls}"><img src="{item}" alt="{item}" class="img-fluid"></div>' for item in items)
            final_content += row.format(row_items=row_items)

        elif block_type == "two-col":
            title = block.get("title", "")
            text = block.get("text", "")
            img = block.get("img", "")
            leftright = block.get("img_position", "")
            if leftright == 'left':
                final_content += two_col_left.format(
                    img=img, title=title, content=text)
            else:
                final_content += two_col_right.format(
                    img=img, title=title, content=text)

        elif block_type == "spacing":
            number = block.get("value", block.get("spacing", 0))
            final_content += mb.format(number=number)

        elif block_type == "scroll_to":
            scroll_to_id = block.get("value", block.get("id", ""))
            final_content += st_id.format(scroll_to_id=scroll_to_id)

        elif block_type == "hero":
            final_content += hero_maker(block)

        elif block_type == "jumbo":
            final_content += jumbotron_maker(block)

        elif block_type == "carousel":
            carousel_html = ''
            width = block.get('width', '')
            height = block.get('height', '')
            carousel_img_list = block.get('content') or block.get('images') or []

            if not carousel_img_list:
                final_content += render_error("carousel", "content/images list is empty")
                continue

            carousel_html += first_frame.format(img_src=carousel_img_list[0], img_width=width, img_height=height)

            for img_src in carousel_img_list[1:]:
                carousel_html += other_frame.format(img_src=img_src, img_width=width, img_height=height)

            final_content += carousel.format(carousel_items=carousel_html, img_width=width, img_height=height)

        elif block_type == "quote":
            final_content += quote_maker(block)

        elif block_type == "cta":
            final_content += cta_maker(block)

        elif block_type == "stats":
            final_content += stats_maker(block)

        elif block_type == "divider":
            final_content += divider_block

        else:
            final_content += render_error("block", f"unsupported block type: {block_type}")

    return final_content
