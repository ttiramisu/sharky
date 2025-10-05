'''
utils/components/footer.py

This file defines the footer component
'''

from datetime import datetime
year = datetime.now().year

nav_title = "{nav_title}"
nav_items = "{nav_items}"

centered_logo = f'''
<div class="container">
  <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <p class="col-md-4 mb-0 text-body-secondary">© {year} {nav_title}</p>
      <img src="">
    <ul class="nav col-md-4 justify-content-end">
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">Home</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">Features</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">Pricing</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">FAQs</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">About</a></li>
    </ul>
  </footer>
</div>
'''

nav_with_name = f'''
<div class="container">
  <footer class="py-3 my-4">
    <ul class="nav justify-content-center border-bottom pb-3 mb-3"> 
      {nav_items}
    </ul>
    <p class="text-center text-body-secondary">© {year} {nav_title}</p>
  </footer>
</div>
'''
