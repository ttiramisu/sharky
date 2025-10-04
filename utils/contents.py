import yaml
from utils.components.row import row
from utils.components.two_col import two_col_img_left as two_col_left
from utils.components.two_col import two_col_img_right as two_col_right
from utils.helper.mb import mb as mb
from utils.helper.scrollto import scroll_to_id as st_id

final_content = ''

with open('./CONTENTS/CONTENTS.yaml', 'r') as file:
    contents = yaml.safe_load(file)

def make_final_content():
    global final_content
    final_content = ''

    for block in contents:
        if "text_row" in block:
            row_list = block['text_row']
            cls = row_list[0].get('class', '')
            items = row_list[1].get('items', [])

            row_items = "".join(f'<div class="col {cls}">{item}</div>' for item in items)
            final_content += row.format(row_items=row_items)

        elif "img_row" in block:
            row_list = block['img_row']
            cls = row_list[0].get('class', '')
            items = row_list[1].get('items', [])

            row_items = "".join(f'<div class="col {cls}"><img src="{item}" alt="{item}" class="img-fluid"></div>' for item in items)
            final_content += row.format(row_items=row_items)

        elif "two-col" in block:
            two_col_list = block["two-col"]
            title, text, img = '', '', ''
            leftright = two_col_list[-1].get('img_position', '')
            for item in two_col_list:
                if 'title' in item:
                    title = item['title']
                elif 'text' in item:
                    text = item['text']
                elif 'img' in item:
                    img = item['img']
            if leftright == 'left':
                final_content += two_col_left.format(img=img, title=title, content=text)
            else:
                final_content += two_col_right.format(img=img, title=title, content=text)

        elif "spacing" in block:
            number = block["spacing"]
            final_content += mb.format(number=number)

        elif "scroll_to" in block:
            scroll_to_id = block['scroll_to']
            final_content += st_id.format(scroll_to_id=scroll_to_id)

    return final_content