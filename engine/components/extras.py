"""
Additional reusable block templates.
"""

quote_block = """
<div class="container my-5">
  <figure class="text-center">
    <blockquote class="blockquote">
      <p>{text}</p>
    </blockquote>
    <figcaption class="blockquote-footer mt-2">
      {author}
    </figcaption>
  </figure>
</div>
"""

cta_block = """
<div class="container my-5">
  <div class="p-5 text-center bg-body-tertiary rounded-3 border">
    <h2 class="mb-3">{title}</h2>
    <p class="lead mb-4">{text}</p>
    <a class="btn btn-primary btn-lg px-4" href="{href}">{button}</a>
  </div>
</div>
"""

stats_block = """
<div class="container my-5">
  <div class="row text-center">
    {items}
  </div>
</div>
"""

stats_item = """
<div class="col-12 col-md-4 mb-4">
  <h3 class="fw-bold mb-1">{value}</h3>
  <p class="text-secondary mb-0">{label}</p>
</div>
"""

divider_block = """
<div class="container my-5">
  <hr class="my-0">
</div>
"""
