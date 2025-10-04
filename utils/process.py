"""
utils/process.py

This module provides helper functions for processing YAML content.
Currently includes:
- process(data): replaces newline characters in strings with <br>
"""

def process(data):
    for key, value in data.items():
        if '\n' in value:
            data[key] = value.replace('\n', '<br>')

    # print(data)