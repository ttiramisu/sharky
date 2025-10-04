import yaml
from utils.process import process
from utils.maker import write_html, generate_html
from utils.structure import add_components_nav_footer

def config():
    with open('CONTENTS/CONFIG.yaml', 'r') as file:
        config_data = yaml.safe_load(file)
    return config_data

# Open the contents file{FOOTER}
def open_contents_file():
    with open('CONTENTS/CONTENTS.yaml', 'r') as file:
        data = yaml.safe_load(file)
    return data

def main():
    config_data = config()

    ''' Process the contents file '''
    content = open_contents_file()
    # process(content)

    ''' Make the html file '''
    nav_content = add_components_nav_footer()
    # print(nav_content[0])
    # print(final_content)
    website_data = generate_html(config_data, nav_content[0], content, nav_content[1])
    write_html(website_data)

if __name__ == "__main__":
    main()
