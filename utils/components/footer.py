'''
this file defines the footer component
'''

from datetime import datetime
year = datetime.now().year

nav_title = "{nav_title}"
nav_items = "{nav_items}"

footer = f'''
<div class="container"> <footer class="py-3 my-4"> <ul class="nav justify-content-center border-bottom pb-3 mb-3"> {nav_items} </ul> <p class="text-center text-body-secondary">© {year} {nav_title}</p> </footer> </div>
'''