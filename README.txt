"""
 This script is responsible for extracting circular features from an image
 using Hough Transform
 Author: Fernando Rodrigues Jr
 Date  : 27/11/2017

"""
# coding=utf-8
# Developed and tested with:
#
# os:             Ubuntu Xenial (16.04)
# python version: Python 3.5.2
# opencv version: 3.3.0

# Notes:
# The code was created using a virtualenv, please run pip install -r requirements.txt
# to run the code: python3 pycv-proj-test.py images/image_filename
#
# Algorithm schema:
# 1 - Image pre-processing ( transform to grayscale, erode/dilate and apply gaussian filter )
# 2 - Feature Extraction ( apply Circular Hough Transform )
# 3 - Show Results
