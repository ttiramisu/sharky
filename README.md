# use yaml to template your websites

## how to use

- clone the github repo
- open the `/CONTENTS` folder
- edit the `/assets/` folder for assets
- edit the `CONFIG.yaml` file for congifuration updates
- edit the `NAVIGATION.yaml` file for editing the navigation
- edit the `CONTENTS.yaml` file for editing the contents (work in progress)

## dev server

- run
  ```bash
  python3 dev.py
  ```
  in the base folder of the project
- the result can be seen in [localhost:6767](localhost:6767) or [http://127.0.0.1:6767/](http://127.0.0.1:6767/)

## production

- run
  ```bash
  python3 main.py
  ```
  in the base folder of the project
- the output will be in the dist folder with the name of `index.html`
- assets are automatically moved into the dist folder for better accesibility

example:

- yaml:

  ```yaml
  - text_row:
      - class: ""
      - items:
          - lorem
          - ipsium
          - dolor

  - img_row:
      - class: ""
      - items:
          - ../assets/img1.jpg
          - ../assets/img2.jpg
          - ../assets/img3.jpg
  ```

- rendered content:

  ```html
  <div class="container text-center">
    <div class="row">
      <div class="col">lorem</div>
      <div class="col">ipsium</div>
      <div class="col">dolor</div>
    </div>
  </div>

  <div class="container text-center">
    <div class="row">
      <div class="col">
        <img src="/assets/img1.jpg" alt="/assets/img1.jpg" class="img-fluid" />
      </div>
      <div class="col">
        <img src="/assets/img2.jpg" alt="/assets/img2.jpg" class="img-fluid" />
      </div>
      <div class="col">
        <img src="/assets/img3.jpg" alt="/assets/img3.jpg" class="img-fluid" />
      </div>
    </div>
  </div>
  ```

## current components

- simple navbar
- simple footer
- text/img rows
- 2 column layouts (img left/img right)
- spacing
- nav scroll to

## note:

- this is still a work in progress, and it may never be finished. use this wisely
- feel free to make your own versions of this
- documentation is not complete
