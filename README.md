# This script is responsible for extracting circular features from an image

    Developed and tested with:
    os:             Ubuntu Xenial (16.04)
    python version: Python 3.5.2
    opencv version: 3.3.0
    
    
## Notes:
The code was created using a virtualenv, please run pip install -r requirements.txt
    
    python3 pycv-proj-test.py images/image_filename

### Algorithm:
 - Image pre-processing ( transform to grayscale, erode/dilate and apply gaussian filter )
 - Feature Extraction ( apply Circular Hough Transform )

![circles_result](https://user-images.githubusercontent.com/3229701/33303592-2a62f070-d3eb-11e7-8b22-8a34cf7f18be.png)
![shapes_leo_result](https://user-images.githubusercontent.com/3229701/33303593-2a985bde-d3eb-11e7-85b7-f67f3834781e.png)
