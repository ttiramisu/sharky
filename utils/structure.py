"""
utils/structure.py

This module provides helper functions for reading components and generating corresponding html.
Currently includes:
- reading components header to replace with actual components
"""

import yaml

from utils.components.header import nav
from utils.components.footer import footer

def add_components_nav_footer():
    with open('./CONTENTS/NAVIGATION.yaml', 'r') as file:
        nav_data = yaml.safe_load(file)

    nav_title = nav_data.get('nav_title', '')

    # Extract items and ids
    nav_items_list = []
    nav_ids_list = []

    for entry in nav_data.get('nav', []):
        if 'items' in entry:
            nav_items_list = entry['items']
        if 'ids' in entry:
            nav_ids_list = entry['ids']

    # Build nav HTML
    nav_items_html = ''
    for item, id_ in zip(nav_items_list, nav_ids_list):
        nav_items_html += f'<li class="nav-item"><a class="nav-link" href="#{id_}">{item}</a></li>'

    nav_html = nav.format(nav_title=nav_title, nav_items=nav_items_html)

    # Build footer HTML
    footer_items_html = ''
    for item, id_ in zip(nav_items_list, nav_ids_list):
        footer_items_html += f'<li class="nav-item"><a class="nav-link px-2 text-body-secondary" href="#{id_}">{item}</a></li>'

    footer_html = footer.format(nav_items=footer_items_html, nav_title=nav_title)

    return nav_html, footer_html