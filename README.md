# use yaml to template your websites

## how to use
- clone the github repo
- open the ```/CONTENTS``` folder
- edit the ```/assets/``` folder for assets (work in progress)
- edit the ```CONFIG.yaml``` file for congifuration updates
- edit the ```NAVIGATION.yaml``` file for editing the navigation
- edit the ```CONTENTS.yaml``` file for editing the contents (work in progress)
- run 
    ```bash
    python3 main.py
    ```
  in the base folder of the project
- the output will be in the dist folder with the name of ```index.html```

example:
- yaml (content)
  ```yaml
  some_content: |
  this is a multi lined
  content

  example_image: "path/to/image"
  ```


## note:
- this is still a work in progress, and it may never be finished. use this wisely
- feel free to make your own versions of this  
