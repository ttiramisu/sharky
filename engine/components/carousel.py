'''
utils/components/carousel.py

This file defines the carousel component
'''


carousel_items = "{carousel_items}"
img_src = "{img_src}"

img_width = "{img_width}"
img_height = "{img_height}"

carousel = '''
<div class="container my-5">
  <div id="carouselExample" class="carousel slide m-auto" style="max-width:{img_width}px; max-height:{img_height}px">
    <div class="carousel-inner">
      {carousel_items}
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</div>
'''

first_frame = '''
<div class="carousel-item active">
  <img src="{img_src}" class="d-block" width="{img_width}px" height="{img_height}px" alt="{img_src}">
</div>
'''

other_frame = '''
<div class="carousel-item">
  <img src="{img_src}" class="d-block" width="{img_width}px" height="{img_height}px" alt="{img_src}">
</div>
'''