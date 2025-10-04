import yaml
from utils.components.row import row

final_content = ''

with open('./CONTENTS/CONTENTS.yaml', 'r') as file:
    contents = yaml.safe_load(file)


def row_maker():
    for key in contents.items():
        if 'text_row' in key:
            row_items = ''
            for item in contents['text_row'].strip().strip('\n').strip('[]').replace("'", "").split(','):
                row_items += f'<div class="col">{item.strip()}</div>'

        row_html = row.format(row_items=row_items)

    global final_content
    final_content += row_html

    for key in contents.items():
        if 'img_row' in key:
            row_items = ''
            for item in contents['img_row'].strip().strip('\n').strip('[]').replace("'", "").split(','):
                row_items += f'<div class="col"><img src="{item.strip()}" alt="{item.strip()}" class="img-fluid")></div>'

        row_html = row.format(row_items=row_items)

    final_content += row_html

def two_col_layout():
    for key in contents.items():
        if 'two_col' in key:
            two_col_items = ''
            for item in contents['two_col'].strip().strip('\n').strip('[]').replace("'", "").split(','):
                two_col_items += f'<div class="col">{item.strip()}</div>'

        two_col_html = two_col.format(row_items=row_items)


def make_final_content():
    row_maker()
    return final_content
