* This script is responsible for extracting circular features from an image

coding=utf-8
Developed and tested with:
os:             Ubuntu Xenial (16.04)
python version: Python 3.5.2
opencv version: 3.3.0

Notes:
The code was created using a virtualenv, please run pip install -r requirements.txt
to run the code: python3 pycv-proj-test.py images/image_filename

* Algorithm schema:
 - Image pre-processing ( transform to grayscale, erode/dilate and apply gaussian filter )
 - Feature Extraction ( apply Circular Hough Transform )
 - Show Results

![alt text](https://github.com/fernandorovai/HoughTransform/tree/master/images/circles_result.png)

![alt text](https://github.com/fernandorovai/HoughTransform/tree/master/images/shapes_leo_result.png)
