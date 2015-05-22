from SimpleCV import *
import cv2
import numpy as np
import sys

cam = Camera()
template = Image("D:/template1.bmp")
template = template.binarize()

while True:
    img = cam.getImage()
    img = img.binarize()

##    res = img.drawKeypointMatches(template,500.00, minDist = 0.1)
##    res.show()
    
##    fs = img.findKeypointMatch(template, quality=500.00, minDist = 0.05, minMatch = 0.9)
##    if (fs is not None):
##        fs.draw()
##    img.show()

    fs = img.findTemplate(template,threshold=15,method="SQR_DIFF_NORM")
    if (fs is not None):
        fs.draw()
    img.show()

