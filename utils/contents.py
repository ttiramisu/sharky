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

final_content = ''

with open('./CONTENTS/CONTENTS.yaml', 'r') as file:
    contents = yaml.safe_load(file)

def hero_maker(block):
    """
    Takes a hero block from YAML and routes it to the correct hero component.
    Buttons with empty text are removed entirely.
    """

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

    # Remove buttons entirely if text is empty
    for btn in ["primary", "secondary"]:
        btn_key = f"btn_{btn}"
        btn_id_key = f"btn_{btn}_id"
        if not hero_data.get(btn_key):
            # Remove the entire <a ...>...</a> tag for this button
            pattern = rf'<a[^>]*{btn_id_key}[^>]*>.*?</a>'
            hero_html = re.sub(pattern, '', hero_html, flags=re.DOTALL)

    # Format remaining placeholders safely
    return hero_html.format_map(defaultdict(str, hero_data))


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

    return final_content
