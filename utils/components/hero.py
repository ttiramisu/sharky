"""
utils/components/hero.py

This module defines the various types of hero layouts
"""

img = '{img}'
title = '{title}'
text = '{text}'
btn_primary = '{btn_primary}'
btn_secondary = '{btn_secondary}'
img_width = '{img_width}'
img_height = '{img_height}'

btn_pri_id = '{btn_primary_id}'
btn_sec_id = '{btn_secondary_id}'

centered_hero = '''
<div class="px-4 py-5 my-5 text-center"> 
  <img class="d-block mx-auto mb-4 img-fluid"
    src="{img}" alt="" width="{img_width}px" height="{img_height}px">
  <h1 class="display-5 fw-bold text-body-emphasis">{title}</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4">{text}</p>
    <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
      <a type="button" class="btn btn-primary btn-lg px-4 gap-3" id="hero-{btn_primary_id}" href="#{btn_primary_id}">
        {btn_primary}
      </a>
      <a type="button" class="btn btn-outline-secondary btn-lg px-4" id="hero-{btn_secondary_id}" href="#{btn_secondary_id}">
        {btn_secondary}
      </a>
    </div>
  </div>
</div>
'''

centered_screenshot = '''
<div class="px-4 pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold text-body-emphasis">{title}</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4">{text}</p>
    <div class="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5">
      <a type="button" class="btn btn-primary btn-lg px-4 me-sm-3" id="hero-{btn_primary_id}" href="#{btn_primary_id}">
        {btn_primary}
      </a>
        
      <a type="button" class="btn btn-outline-secondary btn-lg px-4" id="hero-{btn_secondary_id}" href="#{btn_secondary_id}">
        {btn_secondary}
      </a>
    </div>
  </div>
  <div class="overflow-hidden" style="max-height: 30vh;">
    <div class="container px-5">
      <img src="{img}" class="img-fluid border rounded-3 shadow-lg mb-4"
        alt="{img}" width="{img_width}" height="{img_height}" loading="lazy">
    </div>
  </div>
</div>
'''

text_left_img_right = '''
<div class="container col-xxl-8 px-4 py-5">
  <div class="row flex-lg-row-reverse align-items-center g-5 py-5">
    <div class="col-10 col-sm-8 col-lg-6">
      <img src="{img}" class="d-block mx-lg-auto img-fluid"
        alt="Bootstrap Themes" width="{img_width}px" height="{img_height}px" loading="lazy">
        </div>
    <div class="col-lg-6">
      <h1 class="display-5 fw-bold text-body-emphasis lh-1 mb-3">{title}</h1>
      <p class="lead">{text}</p>
      <div class="d-grid gap-2 d-md-flex justify-content-md-start">
        <a type="button" class="btn btn-primary btn-lg px-4 me-md-2" id="hero-{btn_primary_id}" href="#{btn_primary_id}">
          {btn_primary}
        </a>
        <a type="button" class="btn btn-outline-secondary btn-lg px-4" id="hero-{btn_secondary_id}" href="#{btn_secondary_id}">
          {btn_secondary}
        </a>
      </div>
    </div>
  </div>
</div>
'''

border_crop_img = '''
<div class="container my-5">
  <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
    <div class="col-lg-7 p-3 p-lg-5 pt-lg-3">
      <h1 class="display-4 fw-bold lh-1 text-body-emphasis">{title}</h1>
      <p class="lead">{text}</p>
      <div class="d-grid gap-2 d-md-flex justify-content-md-start mb-4 mb-lg-3">
      <a type="button"
          class="btn btn-primary btn-lg px-4 me-md-2 fw-bold" id="hero-{btn_primary_id}" href="#{btn_primary_id}">{btn_primary}</a>
      <a type="button"
          class="btn btn-outline-secondary btn-lg px-4" id="hero-{btn_secondary_id}" href="#{btn_secondary_id}">{btn_secondary}</a>
      </div>
    </div>
    <div class="col-lg-4 offset-lg-1 p-0 overflow-hidden shadow-lg"> <img class="rounded-lg-3" src="{img}"
        alt="" width="{img_width}px" height="{img_height}px"> </div>
  </div>
</div>
'''
