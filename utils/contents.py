import yaml
from utils.components.row import row
from utils.components.two_col import two_col_img_left as two_col_left
from utils.components.two_col import two_col_img_right as two_col_right
from utils.helper.mb import mb as mb

final_content = ''

with open('./CONTENTS/CONTENTS.yaml', 'r') as file:
    contents = yaml.safe_load(file)


# def row_maker():
#     global final_content

#     for block in contents:
#         if "text_row" in block:
#             row_items = ""
#             for item in block["text_row"]:
#                 row_items += f'<div class="col">{item}</div>'
#             final_content += row.format(row_items=row_items)

#         elif "img_row" in block:
#             row_items = ""
#             for item in block["img_row"]:
#                 row_items += f'<div class="col"><img src="{item}" alt="{item}" class="img-fluid"></div>'
#             final_content += row.format(row_items=row_items)


# def two_col_layout():
#     global final_content

#     for section in contents:
#         if 'two-col' in section:
#             # section['two-col'] is a LIST of dicts
#             block = section['two-col']

#             # Initialize defaults
#             title, text, img = '', '', ''

#             for item in block:
#                 if 'title' in item:
#                     title = item['title']
#                 elif 'text' in item:
#                     text = item['text']
#                 elif 'img' in item:
#                     img = item['img']

#             # Build final HTML
#             two_col_html = two_col.format(img=img, title=title, content=text)
#             final_content += two_col_html

# def margin_bottom():
#     global final_content

#     for section in contents:
#         if 'mb' in section:
#             number = section['mb']
#             mb_html = mb.format(number=number)
#             final_content += mb_html

# def make_final_content():
#     row_maker()
#     two_col_layout()
#     margin_bottom()
#     return final_content

def make_final_content():
    global final_content
    final_content = ''

    for block in contents:
        if "text_row" in block:
            # Extract class and items from the list
            row_list = block['text_row']
            cls = row_list[0].get('class', '')       # first dict is class
            items = row_list[1].get('items', [])     # second dict is items

            row_items = "".join(f'<div class="col">{item}</div>' for item in items)
            final_content += row.format(row_items=row_items)

        elif "img_row" in block:
            row_list = block['img_row']
            cls = row_list[0].get('class', '')
            items = row_list[1].get('items', [])

            row_items = "".join(f'<div class="col"><img src="{item}" alt="{item}" class="img-fluid"></div>' for item in items)
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

    return final_content