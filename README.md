# sharky
A dynamic content-driven web project featuring customizable hero sections, two-column layouts, image and text rows, carousels, and more. The project uses a YAML-based configuration to define page elements, enabling rapid updates and modular content management.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Customization](#customization)
- [License](#license)


## Overview
This project allows you to build modern, responsive web pages using predefined content blocks defined in YAML. Each block represents a UI component, such as a hero section, text block, image row, carousel, or jumbo section. By editing the YAML, you can easily update page content without touching the HTML.

## Features

### Hero Sections
- Types: ```centered_hero```, ```centered_screenshot```, ```text_left_img_right```, ```border_crop_img```

- Customizable fields: ```image```, ```width```, ```height```, ```title```, ```text```, ```primary``` and ```secondary``` buttons with IDs

### Two-Column Layouts
- Flexible content and image placement (left or right)

- Supports text and images with optional spacing

### Jumbo Sections
- Types: ```basic``` or ```full_width```

- Large text sections for highlighting important content

### Rows

- Text Row: Display multiple items in a row

- Image Row: Display multiple images in a row

### Carousel

- Supports multiple images

- Configurable width and height

### Scroll Functionality

- Scroll to a specific element using IDs

### Spacing

- Global spacing control for sections

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/ttiramisu/sharky.git

    cd sharky
    ```
2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Run the development server
    ```bash
    python3 dev.py
    ```
4. Open ```localhost:6767``` in your browser to view your project.

5. To build the project for hosting
    ```bash
    python3 main.py
    ```

## Project Structure

```
sharky/
│
├─ assets/
│  └─ icon.jpg
│
├─ CONTENTS/
│  └─ CONFIG.yaml
│  └─ CONTENTS.yaml
│  └─ NAVIGATION.yaml
│
├─ dist/
│  └─ src/
│  └─ index.html
│
├─ utils/
│  └─ components/        # defines all components
│  └─ helper/            # defines all helper components
│  └─ contents.py        # generates the contents in the final file
│  └─ maker.py           # defines and generates the html frame
│  └─ structure.py       # generates the navbar and footer of the final file
│
├─ dev.py
├─ main.py
├─ requirements.txt
└─ README.md
```

## Usage
1. Open ```CONTENTS/CONTENTS.yaml``` and define your sections.

2. Supported content blocks:

| Block Type  | Description                               |
| ----------- | ----------------------------------------- |
| `hero`      | Highlighted section with optional buttons |
| `two-col`   | Two-column layout with text and images    |
| `text_row`  | Row of text items                         |
| `img_row`   | Row of images                             |
| `carousel`  | Scrollable image carousel                 |
| `jumbo`     | Large text sections                       |
| `spacing`   | Custom spacing between sections           |
| `scroll_to` | ID for scroll navigation                  |

3. Open ```CONTENTS/CONFIG.yaml``` and define your global website settings.
4. Required Fields:

| Field          | Description                                    |
| -------------- | ---------------------------------------------- |
| `language`     | Website language (ISO code)                    |
| `website-name` | The name of your website                       |
| `website-icon` | Path to the site icon                          |
| `description`  | Meta description for SEO                       |
| `custom_css`   | Optional path to a CSS file for custom styling |

Eample:
```yaml
language: en
website-name: Lorem Ipsium
website-icon: src/assets/icon.jpg
description: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
custom_css: src/css/style.css
```

5. Open ```CONTENTS/NAVIGATION.yaml``` and define your website’s navigation menu, including nested items and IDs for links.
6. Required Fields:

| Field       | Description                                                                |
| ----------- | -------------------------------------------------------------------------- |
| `nav_title` | Title or brand of the navigation bar                                       |
| `logo`      | Path to the logo image                                                     |
| `nav`       | List of navigation items and their structure                               |
| `ids`       | Corresponding IDs for each navigation item (used for scrolling or linking) |

Example:
```yaml
nav_title: nav example
logo: src/assets/icon.jpg
nav:
  - items:
      - nav1:
          - sub1
          - sub2
          - sub3
      - nav2
      - nav3
      - nav4
  - ids:
      - nav1:
          - sub1
          - sub2
          - sub3
      - nav2
      - susan
      - shelia
```
Notes:
- Menu labels in nav must have matching entries in ids for proper scrolling or linking functionality.
- Submenus allow multi-level navigation. Example: nav1 → sub1, sub2, sub3.
- Top-level items like nav2, nav3, nav4 can directly link to IDs or sections on the page.

## Required Fields for Each Content Block
To ensure each block renders properly, the following fields must be in your YAML:

### 1. Hero Blocks (hero)
#### - Required Fields:

- ```type``` → ```centered_hero```, ```centered_screenshot```, ```text_left_img_right```, or ```border_crop_img```
- ```img``` → Path to the image
- ```img_width``` → Width of the image in pixels
- ```img_height``` → Height of the image in pixels
- ```title``` → Heading text
- ```text``` → Main paragraph or description

#### - Optional Fields:

- ```btn_primary``` → Label for primary button
- ```btn_secondary``` → Label for secondary button
- ```btn_primary_id``` → ID for primary button (used for scroll or JS actions)
- ```btn_secondary_id``` → ID for secondary button

Example:
```yaml
- hero:
  - type: centered_hero
  - img: src/assets/icon.jpg
  - img_width: 57
  - img_height: 500
  - title: Lorem Ipsium
  - text: |
      lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  - btn_primary: Primary Button
  - btn_secondary: 
  
  - btn_primary_id: lorem-right
  - btn_secondary_id: 
```

### 2. Two-Column Layout (two-col)

#### - Required Fields:

- ```title``` → Heading text
- ```text``` → Description or paragraph
- ```img``` → Path to image
- ```img_position``` → left or right

#### - Optional Fields:

- ```class``` → CSS class for styling

Example:
```yaml
- two-col:
  - class: ''
  - title: lorem ipsum
  - text: |
      lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  - img : src/assets/icon.jpg
  - img_position : left
```

### 3. Jumbo Section (jumbo)

#### - Required Fields:

- ```type``` → basic or full_width
- ```title``` → Heading text
- ```text``` → Paragraph text

Example:
```yaml
- jumbo:
  - type: full_width 
  - title: lorem ipsum
  - text: |
      lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

### 4. Text Row (text_row)

#### - Required Fields:
- ```items``` → List of text items

#### - Optional Fields:
- ```class``` → CSS class for styling

Example:
```yaml
- text_row:
  - class: 'johnny'
  - items:
    - john
    - peter
    - susan
```

### 5. Image Row (img_row)

#### - Required Fields:
- ```items``` → List of image paths

#### - Optional Fields:
- ```class``` → CSS class for styling

Example:
```yaml
- img_row: 
  - class: ''
  - items:
    - src/assets/icon.jpg
    - src/assets/icon.jpg
    - src/assets/icon.jpg
```

### 6. Carousel (carousel)

#### - Required Fields:

- ```content``` → List of image paths
- ```width``` → Carousel width in pixels
- ```height``` → Carousel height in pixels

Example:
```yaml
- carousel:
  - content:
    - src/assets/icon.jpg
    - src/assets/icon.jpg
    - src/assets/icon.jpg
  - width: 500
  - height: 100
```

### 7. Spacing (spacing)

#### - Required Fields:
- ```spacing``` → Represents spacing between sections in pixels

Example:
```yaml
- spacing: 50
```

### 8. Scroll Target (scroll_to)

#### - Required Fields:
- ```scroll_to``` → ID of the element you want to scroll to (must match a btn_primary_id, btn_secondary_id or a ids in NAVIGATION.yaml)

Example:
```yaml
- scroll_to: lorem-right
```

## Customization
- Update hero images, titles, and buttons directly in YAML.

- Modify the number of items in text or image rows.

- Adjust carousel width, height, and images.

- Set global spacing between sections for visual layout consistency.

## License
MIT License. See ```LICENSE``` file for details.