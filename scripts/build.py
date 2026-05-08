import shutil
import sys
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from engine.contents import make_final_content
from engine.maker import generate_html, write_html
from engine.structure import make_footer, make_nav

SRC_ASSETS = PROJECT_ROOT / "web"
DIST_DIR = PROJECT_ROOT / "dist"
DEST_ASSETS = PROJECT_ROOT / "dist" / "web"
CONFIG_PATH = PROJECT_ROOT / "content" / "CONFIG.yaml"
DEFAULT_CONTENT_PATH = PROJECT_ROOT / "content" / "CONTENTS.yaml"
DEFAULT_NAVIGATION_PATH = PROJECT_ROOT / "content" / "NAVIGATION.yaml"


def config():
    try:
        with open(CONFIG_PATH, "r") as file:
            config_data = yaml.safe_load(file) or {}
    except FileNotFoundError as err:
        raise RuntimeError(f"Missing config file: {CONFIG_PATH}") from err
    except yaml.YAMLError as err:
        raise RuntimeError(f"Invalid YAML in config file: {CONFIG_PATH}") from err
    if not isinstance(config_data, dict):
        raise RuntimeError(f"Config root must be a mapping: {CONFIG_PATH}")
    return config_data


def resolve_content_path(path_value):
    if not path_value:
        return DEFAULT_CONTENT_PATH

    path = Path(path_value)
    if path.is_absolute():
        return path
    if (PROJECT_ROOT / path).exists():
        return PROJECT_ROOT / path
    return PROJECT_ROOT / "content" / path


def resolve_navigation_path(path_value):
    if not path_value:
        return DEFAULT_NAVIGATION_PATH

    path = Path(path_value)
    if path.is_absolute():
        return path
    if (PROJECT_ROOT / path).exists():
        return PROJECT_ROOT / path
    return PROJECT_ROOT / "content" / path


def build_page_config(global_config, page):
    page_config = {k: v for k, v in global_config.items() if k != "pages"}
    page_config.update(page.get("config", {}))

    for key in ("language", "website-name", "website-icon", "description", "custom_css"):
        if key in page:
            page_config[key] = page[key]
    if "title" in page:
        page_config["website-name"] = page["title"]

    return page_config


def pages_from_config(config_data):
    configured_pages = config_data.get("pages")
    if isinstance(configured_pages, list) and configured_pages:
        pages = []
        for page in configured_pages:
            if not isinstance(page, dict):
                raise RuntimeError("Each entry in 'pages' must be a mapping")
            output = str(page.get("output", "index.html")).strip()
            if not output:
                raise RuntimeError("Page output cannot be empty")
            if not output.endswith(".html"):
                raise RuntimeError(f"Page output must end with .html: {output}")
            pages.append({
                "output": output,
                "content_path": resolve_content_path(page.get("content")),
                "navigation_path": resolve_navigation_path(page.get("navigation")),
                "config": build_page_config(config_data, page),
            })
        if pages:
            return pages

    return [{
        "output": "index.html",
        "content_path": DEFAULT_CONTENT_PATH,
        "navigation_path": DEFAULT_NAVIGATION_PATH,
        "config": {k: v for k, v in config_data.items() if k != "pages"},
    }]


def main():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)

    shutil.copytree(SRC_ASSETS, DEST_ASSETS)

    config_data = config()
    pages = pages_from_config(config_data)

    for page in pages:
        if not page["content_path"].exists():
            raise RuntimeError(f"Page content file not found: {page['content_path']}")
        if not page["navigation_path"].exists():
            raise RuntimeError(f"Page navigation file not found: {page['navigation_path']}")
        content = make_final_content(page["content_path"])
        nav_content = make_nav(page["navigation_path"])
        footer_content = make_footer(page["navigation_path"])
        website_data = generate_html(page["config"], nav_content, content, footer_content)
        write_html(website_data, page["output"])

if __name__ == "__main__":
    main()
