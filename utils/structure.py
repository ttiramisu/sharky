"""
utils/structure.py

This module provides helper functions for reading components and generating corresponding html.
Currently includes:
- reading components header and footer to replace with actual components
"""

import yaml
from utils.components.header import nav
from utils.components.footer import footer

def make_footer():
    """
    make the footer based on NAVIGATION.yaml
    """

    with open('./CONTENTS/NAVIGATION.yaml', 'r') as file:
        footer_data = yaml.safe_load(file)

    nav_title = footer_data.get('nav_title', '')
    logo = footer_data.get('logo', '')

    nav_items_list, nav_ids_list = [], []
    for entry in footer_data.get('nav', []):
        if 'items' in entry:
            nav_items_list = entry['items']
        if 'ids' in entry:
            nav_ids_list = entry['ids']

    footer_items_html = ''
    for item, id_ in zip(nav_items_list, nav_ids_list):
        if isinstance(item, dict) and isinstance(id_, dict):
            parent_item, sub_items = list(item.items())[0]
            parent_id, sub_ids = list(id_.items())[0]

            # footer_items_html += f'<li class="nav-item"><a class="nav-link px-2 text-body-secondary" href="#{parent_id}">{parent_item}</a></li>'

            for sub_item, sub_id in zip(sub_items, sub_ids):
                holder = f'{parent_item} > {sub_item}'
                footer_items_html += f'<li class="nav-item"><a class="nav-link px-2 text-body-secondary" href="#{sub_id}">{holder}</a></li>'
        else:
            footer_items_html += f'<li class="nav-item"><a class="nav-link px-2 text-body-secondary" href="#{id_}">{item}</a></li>'

    logo_html = f'<img src="{logo}" alt="logo" width="40" height="40" class="d-inline-block align-text-top me-2">' if logo else ''

    footer_html = footer.format(nav_title=nav_title,
                          nav_items=footer_items_html, nav_img=logo_html)

    return footer_html

def make_nav():
    """
    make the navigation based on NAVIGATION.yaml
    """

    with open('./CONTENTS/NAVIGATION.yaml', 'r') as file:
        nav_data = yaml.safe_load(file)

    nav_title = nav_data.get('nav_title', '')
    logo = nav_data.get('logo', '')   # <— new

    if logo:
        logo_html = f'<img src="{logo}" alt="logo" width="30" height="30" class="d-inline-block align-text-top me-2">'
    else:
        logo_html = ''  # nothing rendered

    # Extract items and ids
    nav_items_list, nav_ids_list = [], []
    for entry in nav_data.get('nav', []):
        if 'items' in entry:
            nav_items_list = entry['items']
        if 'ids' in entry:
            nav_ids_list = entry['ids']

    # Build nav HTML (same dropdown logic as before)
    nav_items_html = ''
    for item, id_ in zip(nav_items_list, nav_ids_list):
        if isinstance(item, dict) and isinstance(id_, dict):
            parent_item, sub_items = list(item.items())[0]
            parent_id, sub_ids = list(id_.items())[0]
            sub_html = ''.join(
                f'<li><a class="dropdown-item" href="#{sub_id}">{sub_item}</a></li>'
                for sub_item, sub_id in zip(sub_items, sub_ids)
            )
            nav_items_html += f'''
            <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#{parent_id}" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                {parent_item}
            </a>
            <ul class="dropdown-menu">
                {sub_html}
            </ul>
            </li>'''
        else:
            nav_items_html += f'<li class="nav-item"><a class="nav-link" href="#{id_}">{item}</a></li>'

    # ✅ include logo now
    nav_html = nav.format(nav_title=nav_title,
                          nav_items=nav_items_html, nav_img=logo_html)

    return nav_html