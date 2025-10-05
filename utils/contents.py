'''
utils/contents.py

This module provides the function to read the CONTENTS.yaml file and process them into actual html
'''

import yaml
from collections import defaultdict
import re

# CUSTOM COMPONENTS
from utils.components.row import row
from utils.components.two_col import two_col_img_left as two_col_left
from utils.components.two_col import two_col_img_right as two_col_right
from utils.helper.mb import mb as mb
from utils.helper.scrollto import scroll_to_id as st_id

# HERO COMPONENTS
from utils.components.hero import centered_hero, centered_screenshot, text_left_img_right, border_crop_img

# JUMBOTRON COMPONENTS
from utils.components.jumbo import basic, full_width

# CAROUSEL COMPONENTS
from utils.components.carousel import carousel, first_frame, other_frame

final_content = ''

with open('./CONTENTS/CONTENTS.yaml', 'r') as file:
    contents = yaml.safe_load(file)


def hero_maker(block):
    """
    Takes a hero block from YAML and routes it to the correct hero component.
    Buttons with empty text are removed entirely.
    Images with no value are also removed.
    """
    import re
    from collections import defaultdict

    # Flatten YAML list-of-dicts into a single dict
    hero_data = {}
    for item in block["hero"]:
        if isinstance(item, dict):
            hero_data.update(item)

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

    # 🔹 Remove <img> tags if the image data is empty
    for img in ["primary", "secondary"]:
        img_key = f"img_{img}"
        img_id_key = f"img_{img}_id"
        if not hero_data.get(img_key):
            pattern = rf'<img[^>]*{img_id_key}[^>]*>'
            hero_html = re.sub(pattern, '', hero_html, flags=re.DOTALL)

    # 🔹 Remove buttons entirely if text is empty
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

    jumbo_data = {}
    for item in block.get("jumbo", []):
        if isinstance(item, dict):
            jumbo_data.update(item)

    jumbo_type = jumbo_data.get("type", "basic").lower()
    jumbotron_html = jumbotron_map.get(jumbo_type)

    if not jumbotron_map:
        return f"<!-- Unknown jumbotron type: {jumbo_type} -->"

    return jumbotron_html.format_map(defaultdict(str, jumbo_data))

def make_final_content():
    global final_content
    final_content = ''

    for block in contents:
        if "text_row" in block:
            row_list = block['text_row']
            cls = row_list[0].get('class', '')
            items = row_list[1].get('items', [])

            row_items = "".join(
                f'<div class="col {cls}">{item}</div>' for item in items)
            final_content += row.format(row_items=row_items)

        elif "img_row" in block:
            row_list = block['img_row']
            cls = row_list[0].get('class', '')
            items = row_list[1].get('items', [])

            row_items = "".join(
                f'<div class="col {cls}"><img src="{item}" alt="{item}" class="img-fluid"></div>' for item in items)
            final_content += row.format(row_items=row_items)

        elif "two-col" in block:
            two_col_list = block["two-col"]
            title, text, img = '', '', ''
            leftright = two_col_list[-1].get('img_position', '')
            for item in two_col_list:
                if 'title' in item:
                    title = item['title']
                elif 'text' in item:
                    text = item['text']
                elif 'img' in item:
                    img = item['img']
            if leftright == 'left':
                final_content += two_col_left.format(
                    img=img, title=title, content=text)
            else:
                final_content += two_col_right.format(
                    img=img, title=title, content=text)

        elif "spacing" in block:
            number = block["spacing"]
            final_content += mb.format(number=number)

        elif "scroll_to" in block:
            scroll_to_id = block['scroll_to']
            final_content += st_id.format(scroll_to_id=scroll_to_id)

        elif "hero" in block:
            final_content += hero_maker(block)

        elif "jumbo" in block:
            final_content += jumbotron_maker(block)

        elif "carousel" in block:
            carousel_html = ''
            carousel_data_list = block['carousel']
            carousel_data = {}

            for item in carousel_data_list:
                if isinstance(item, dict):
                    carousel_data.update(item)

            width = carousel_data.get('width', '')
            height = carousel_data.get('height', '')

            carousel_img_list = carousel_data.get('content', [])

            carousel_html += first_frame.format(img_src=carousel_img_list[0], img_width=width, img_height=height)

            for img_src in carousel_img_list[1:]:
                carousel_html += other_frame.format(img_src=img_src, img_width=width, img_height=height)

            final_content += carousel.format(carousel_items=carousel_html, img_width=width, img_height=height)

    return final_content
