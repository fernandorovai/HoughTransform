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

import cv2                           #opencv for image processing
import numpy as np                   #np for array / matrix handling
import sys                           #read external parameters
import copy                          #copy the image to show original and processed
from matplotlib import pyplot as plt #matplotlib for showing the results (plots)


class circleDetector:

    def __init__(self, imgPath):
        self._originalImg = cv2.imread(imgPath)

    def imgPreProcessing(self, originalImg):
        # Setup kernels
        gaussianKernelSize      = (5,5)
        grayImg                 = cv2.cvtColor(originalImg, cv2.COLOR_BGR2GRAY)
        ellipseKernel           = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

        # Morph_Gradiente - Difference between dilation and erosion
        # Morph Close - Erode and Dilate to help eliminating aliasing
        diff = cv2.morphologyEx(grayImg, cv2.MORPH_GRADIENT,ellipseKernel)
        result = cv2.morphologyEx(diff, cv2.MORPH_CLOSE,ellipseKernel)

        # Using a gaussian filter to blur the image in order to
        # reduce noise.
        blurImg = cv2.GaussianBlur(result, gaussianKernelSize, 1)
        return blurImg

    def extractFeature(self, preprocessedImg, originalImg):
        centerColor     = (255,255,255)    # White
        circleColor     = (255,0,0)        # Blue
        centerThickness = 2
        circleThickness = 3

        # Extract feature
        circles = cv2.HoughCircles(preprocessedImg,cv2.HOUGH_GRADIENT,1.2, 200, param1=20, param2=90, minRadius=10, maxRadius=100)

        # New copy from original image to draw the circles
        processedImg = copy.copy(originalImg)

        # Draw circles and centers
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                if i[2] < 10:
                    print("Radius is smaller than 10 pixels")
                    exit()
                # draw circles
                cv2.circle(processedImg,(i[0],i[1]),i[2],circleColor, circleThickness)
                # draw centers
                cv2.circle(processedImg,(i[0],i[1]),2,centerColor, centerThickness)
        return processedImg

    def showResults(self, processedImg, originalImg):
        fig = plt.figure()

        fig1 = fig.add_subplot(121)
        fig1.set_axis_off()
        fig1.set_title("Original Image")
        fig1.imshow(cv2.cvtColor(self._originalImg, cv2.COLOR_BGR2RGB))

        fig2 = fig.add_subplot(122)
        fig2.set_axis_off()
        fig2.set_title("Processed Image")
        fig2.imshow(cv2.cvtColor(processedImg, cv2.COLOR_BGR2RGB))
        plt.show()

    # Process the steps
    # 1 - Image pre-processing ( transform to grayscale, erode/dilate and apply gaussian filter )
    # 2 - Feature Extraction ( apply Circular Hough Transform )
    # 3 - Show Results
    def process(self):
        preprocessedImg = self.imgPreProcessing(self._originalImg)
        processedImg    = self.extractFeature(preprocessedImg, self._originalImg)
        self.showResults(processedImg, self._originalImg)

if __name__ == "__main__":
    param = sys.argv
    if len(param) > 1:
        detector = circleDetector(param[1])
        detector.process()
    else:
        print("Please, insert images/filename as command parameter")

