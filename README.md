current ideas
- md/yaml file formats to put content
- custom variables linked to files to render content

  or

- custom blocks to render files

example

- HTML file
  ```html
  <div>
    { some_content }
    { example_image }
  </div>
  ```
- yaml (content)
  ```yaml
  some_content: |
  this is a multi lined
  content

  example_image: "path/to/image"
  ```
  or
- md (content)
  ```md
  ::some_content
  this is a multi lined
  content
  ::

  ::example_image
  path/to/image
  ::
  ```

  output
  ```html
  <div>
    this is a multi lined
    content

    <img src="path/to/image" alt="image">
  </div>
  ```

  
