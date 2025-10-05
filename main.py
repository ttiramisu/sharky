import yaml
import os
import shutil

from utils.maker import write_html, generate_html
from utils.structure import make_nav, make_footer
from utils.contents import make_final_content

SRC_ASSETS = "src"
DEST_ASSETS = "dist/src"

def config():
    with open('CONTENTS/CONFIG.yaml', 'r') as file:
        config_data = yaml.safe_load(file)
    return config_data

def main():
    if os.path.exists(DEST_ASSETS):
        shutil.rmtree(DEST_ASSETS)
    
    shutil.copytree(SRC_ASSETS, DEST_ASSETS)

    config_data = config()

    ''' Process the contents file '''
    content = make_final_content()

    ''' Make the html file '''
    nav_content = make_nav()
    footer_content = make_footer()
    website_data = generate_html(config_data, nav_content, content, footer_content)
    write_html(website_data)

if __name__ == "__main__":
    main()
