'''
utils/components/footer.py

This file defines the footer component
'''

from datetime import datetime
year = datetime.now().year

footer_title = "{nav_title}"
footer_items = "{nav_items}"
logo_html = "{nav_img}"

footer = f'''
<div class="container">
  <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <p class="col-md-4 mb-0 text-body-secondary">© {year} {footer_title}</p>
    {logo_html}
    <ul class="nav col-md-4 justify-content-end">
      {footer_items}
    </ul>
  </footer>
</div>
'''
