"""
utils/maker.py

This module provides helper functions for turning YAML content into a html file.
Currently includes:
- adding the configuration values to the html file
- adding the already processed contents to the html file
"""

import html
import os

def generate_html(config, HEADER, content, FOOTER):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="{html.escape(config.get('language', 'en'))}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{html.escape(config.get('website-name', 'My Website'))}</title>
        <link rel="icon" href="{html.escape(config.get('website-icon'))}">
        <meta name="description" content="{html.escape(config.get('description', ''))}">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        {HEADER}
        {content}
        {FOOTER}
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return html_template

def write_html(data):
    os.makedirs('dist', exist_ok=True)
    file_path = os.path.join('dist', 'index.html')
    with open(file_path, 'w') as file:
        file.write(data)