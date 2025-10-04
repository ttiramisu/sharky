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
    '''
    Adds the navigation bar to the html file by reading the NAVIGATION.yaml file.
    '''

    with open('./CONTENTS/NAVIGATION.yaml', 'r') as file:
        nav_data = yaml.safe_load(file)

    for key in nav_data.items():
        if 'nav_title' in key:
            nav_title = nav_data['nav_title']
            nav_items = ''
            for item in nav_data['nav'].strip('\n').strip('[]').replace("'", "").split(','):
                nav_items += f'<li class="nav-item"><a class="nav-link" href="#{item.strip()}">{item.strip()}</a></li>'
            
            nav_html = nav.format(nav_title=nav_title, nav_items=nav_items)

            nav_items = ''
            for item in nav_data['nav'].strip().strip('\n').strip('[]').replace("'", "").split(','):
                nav_items += f'<li class="nav-item"><a class="nav-link px-2 text-body-secondary" href="#{item.strip()}">{item.strip()}</a></li>'

            footer_html = footer.format(nav_items=nav_items, nav_title=nav_title)
    
    return nav_html, footer_html