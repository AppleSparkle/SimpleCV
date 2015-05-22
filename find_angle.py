from SimpleCV import *
import sys, time, math

import cv2
import numpy as np
import itertools

cam = Camera()

coord = [1,2,3,4]
templ1 = Image("D:/tmpl1.bmp")
templ2 = Image("D:/tmpl2.bmp")
t = 7

while TRUE:
    
    img = cam.getImage()

##    fs = img.findKeypointMatch(templ1,300.00,0.5,0.1)
##    if (fs is not None):
##        fs.draw()
##    img.show()


##    fs1 = img.findTemplate(templ1,threshold=t,method="SQR_DIFF_NORM")
##    fs2 = img.findTemplate(templ2,threshold=t,method="SQR_DIFF_NORM")
##
##    t1_count = 0
##    t2_count = 0
##    i = 0
##    
##    for match in fs1:
##        img.drawRectangle(match.x,match.y,match.width(),match.height(),color=Color.RED)
##        img.drawText("template1", match.x,match.y,color=Color.RED, fontsize = 32)
##        #crop_t1 = img.crop(match.x,match.y,match.width(),match.height())
##        coord[i] = match.x
##        coord[i+1] = match.y
##        t1_count = t1_count + 1
##
##    i = 2
##    for match in fs2:
##        img.drawRectangle(match.x,match.y,match.width(),match.height(),color=Color.BLUE)
##        img.drawText("template2", match.x,match.y,color=Color.BLUE, fontsize = 32)
##        #crop_t2 = img.crop(match.x,match.y,match.width(),match.height())
##        coord[i] = match.x
##        coord[i+1] = match.y
##        t2_count = t2_count + 1
##
##
##
##    if (t1_count == 1 and t2_count == 1):
##        img.drawLine((coord[0],coord[1]),(coord[2],coord[3]),color=Color.RED,thickness=5)
##                
##        coord[0]=float(coord[0])
##        coord[1]=float(coord[1])
##        coord[2]=float(coord[2])
##        coord[3]=float(coord[3])
##        
##        dy = math.fabs(coord[1]-coord[3])
##        dx = math.fabs(coord[0]-coord[2])
##        
##        
##        angle = math.atan(dy/dx)*180/math.pi
##        img.drawText(str(angle), fontsize = 32)
##
##        
##
##    img.show()






    
    img = img.binarize()
    img = img.invert()
    blobs = img.findBlobs(minsize=300)
    
    i=0
    if blobs:
        for blob in blobs:
            coord[i] = blob.coordinates()[0]
            coord[i+1] = blob.coordinates()[1]
            i=i+2
            if i==4:
                break

       
    if i==4:
        img.drawLine((coord[0],coord[1]),(coord[2],coord[3]),color=Color.RED,thickness=5)
                
        coord[0]=float(coord[0])
        coord[1]=float(coord[1])
        coord[2]=float(coord[2])
        coord[3]=float(coord[3])
        
        dy = math.fabs(coord[1]-coord[3])
        dx = math.fabs(coord[0]-coord[2])

        if dx!=0:
            angle = math.atan(dy/dx)*180/math.pi
            img.drawText(str(angle), fontsize = 32)

    img.show()
    


