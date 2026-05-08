"""
utils/structure.py

This module provides helper functions for reading components and generating corresponding html.
Currently includes:
- reading components header and footer to replace with actual components
"""

import yaml
from pathlib import Path

from engine.components.footer import footer
from engine.components.header import nav

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NAVIGATION_PATH = PROJECT_ROOT / "content" / "NAVIGATION.yaml"


def parse_navigation_items(nav_data):
    """
    Support both schemas:
    1) New:
       items:
         - label: Home
           id: home
         - label: Products
           id: products
           children:
             - label: Product A
               id: product-a
    2) Legacy:
       nav:
         - items: [...]
         - ids:   [...]
    """

    items = nav_data.get("items")
    if isinstance(items, list):
        normalized = []
        for item in items:
            if not isinstance(item, dict):
                continue
            label = item.get("label", "")
            item_id = item.get("id", "")
            href = item.get("href", "")
            children = []
            for child in item.get("children", []):
                if not isinstance(child, dict):
                    continue
                children.append({
                    "label": child.get("label", ""),
                    "id": child.get("id", ""),
                    "href": child.get("href", ""),
                })
            normalized.append({"label": label, "id": item_id, "href": href, "children": children})
        return normalized

    nav_items_list, nav_ids_list = [], []
    for entry in nav_data.get('nav', []):
        if 'items' in entry:
            nav_items_list = entry['items']
        if 'ids' in entry:
            nav_ids_list = entry['ids']

    normalized = []
    for item, id_ in zip(nav_items_list, nav_ids_list):
        if isinstance(item, dict) and isinstance(id_, dict):
            parent_item, sub_items = list(item.items())[0]
            parent_id, sub_ids = list(id_.items())[0]
            children = [{"label": sub_item, "id": sub_id, "href": ""} for sub_item, sub_id in zip(sub_items, sub_ids)]
            normalized.append({"label": parent_item, "id": parent_id, "href": "", "children": children})
        else:
            normalized.append({"label": item, "id": id_, "href": "", "children": []})

    return normalized


def _resolve_href(item):
    href = item.get("href", "")
    if href:
        return href
    item_id = item.get("id", "")
    if item_id:
        return f"#{item_id}"
    return "#"


def _load_navigation_data(navigation_path=None):
    nav_path = Path(navigation_path) if navigation_path else NAVIGATION_PATH
    if not nav_path.is_absolute():
        nav_path = PROJECT_ROOT / nav_path
    with open(nav_path, "r") as file:
        return yaml.safe_load(file) or {}


def make_footer(navigation_path=None):
    """
    make the footer based on NAVIGATION.yaml
    """

    footer_data = _load_navigation_data(navigation_path)

    nav_title = footer_data.get('nav_title', '')
    logo = footer_data.get('logo', '')

    nav_items = parse_navigation_items(footer_data)

    footer_items_html = ''
    for item in nav_items:
        label = item.get("label", "")
        item_id = item.get("id", "")
        children = item.get("children", [])
        if children:
            for child in children:
                holder = f'{label} > {child.get("label", "")}'
                footer_items_html += f'<li class="nav-item"><a class="nav-link px-2 text-body-secondary" href="{_resolve_href(child)}">{holder}</a></li>'
        else:
            footer_items_html += f'<li class="nav-item"><a class="nav-link px-2 text-body-secondary" href="{_resolve_href(item)}">{label}</a></li>'

    logo_html = f'<img src="{logo}" alt="logo" width="40" height="40" class="d-inline-block align-text-top me-2">' if logo else ''

    footer_html = footer.format(nav_title=nav_title,
                          nav_items=footer_items_html, nav_img=logo_html)

    return footer_html

def make_nav(navigation_path=None):
    """
    make the navigation based on NAVIGATION.yaml
    """

    nav_data = _load_navigation_data(navigation_path)

    nav_title = nav_data.get('nav_title', '')
    logo = nav_data.get('logo', '')   # <— new

    if logo:
        logo_html = f'<img src="{logo}" alt="logo" width="30" height="30" class="d-inline-block align-text-top me-2">'
    else:
        logo_html = ''  # nothing rendered

    nav_items = parse_navigation_items(nav_data)

    # Build nav HTML (same dropdown logic as before)
    nav_items_html = ''
    for item in nav_items:
        label = item.get("label", "")
        item_id = item.get("id", "")
        children = item.get("children", [])
        if children:
            sub_html = ''.join(
                f'<li><a class="dropdown-item" href="{_resolve_href(child)}">{child.get("label", "")}</a></li>'
                for child in children
            )
            nav_items_html += f'''
            <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="{_resolve_href(item)}" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                {label}
            </a>
            <ul class="dropdown-menu">
                {sub_html}
            </ul>
            </li>'''
        else:
            nav_items_html += f'<li class="nav-item"><a class="nav-link" href="{_resolve_href(item)}">{label}</a></li>'

    # ✅ include logo now
    nav_html = nav.format(nav_title=nav_title,
                          nav_items=nav_items_html, nav_img=logo_html)

    return nav_html
