'''
utils/components/header.py

This file defines the header component
'''

nav_title = "{nav_title}"
nav_items = "{nav_items}"

nav = f'''
<div class="sticky-top">
    <nav class="navbar navbar-expand-lg bg-body-tertiary" id="nav">
      <div class="container">
        <a class="navbar-brand" href="#">
          {nav_title}
        </a>
        <button class=" navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto">
          {nav_items}
          </ul>
        </div>
      </div>
    </nav>
  </div>
'''