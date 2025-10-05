"""
utils/components/two_col.py

This module provides helper functions for adding the two column layout
"""

img = "{img}"
title = "{title}"
content = "{content}"

two_col_img_left = '''
<div class="container mb-5">
  <div class="row gy-3 gy-md-4 gy-lg-0 align-items-lg-center">
    <div class="container col-12 col-lg-6 col-xl-5 justify-content-end">
      <div class="">
        <img class="img-fluid rounded" loading="lazy" src="{img}" alt="{img}">
      </div>
    </div>
    <div class="col-12 col-lg-6 col-xl-7">
      <div class="row justify-content-xl-center">
        <div class="col-12 col-xl-11">
          <h2 class="mb-3" id="intro">{title}</h2>
          <p class="lead fs-5 text-secondary mb-3">
            {content}
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
'''

two_col_img_right = f'''
<div class="container mb-5">
  <div class="row gy-3 gy-md-4 gy-lg-0 align-items-lg-center">
    <div class="col-12 col-lg-6 col-xl-7">
      <div class="row justify-content-xl-center">
        <div class="col-12 col-xl-11">
          <h2 class="mb-3" id="intro">{title}</h2>
          <p class="lead fs-5 text-secondary mb-3">
            {content}
          </p>
        </div>
      </div>
    </div>
    <div class="container col-12 col-lg-6 col-xl-5 justify-content-end">
      <div class="">
        <img class="img-fluid rounded" loading="lazy" src="{img}" alt="{img}">
      </div>
    </div>
  </div>
</div>
'''
