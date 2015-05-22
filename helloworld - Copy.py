from SimpleCV import *
from numpy import *
import numpy as np
import cv2
from common import anorm
from functools import partial


FLANN_INDEX_KDTREE = 1  # bug: flann enums are missing

flann_params = dict(algorithm = FLANN_INDEX_KDTREE,
                    trees = 4)

def match_bruteforce(desc1, desc2, r_threshold = 0.75):
    res = []
    for i in xrange(len(desc1)):
        dist = anorm( desc2 - desc1[i] )
        n1, n2 = dist.argsort()[:2]
        r = dist[n1] / dist[n2]
        if r < r_threshold:
            res.append((i, n1))
    return np.array(res)

def match_flann(desc1, desc2, r_threshold = 0.6):
    flann = cv2.flann_Index(desc2, flann_params)
    idx2, dist = flann.knnSearch(desc1, 2, params = {}) # bug: need to provide empty dict
    mask = dist[:,0] / dist[:,1] < r_threshold
    idx1 = np.arange(len(desc1))
    pairs = np.int32( zip(idx1, idx2[:,0]) )
    return pairs[mask]

def draw_match(img1, img2, p1, p2, status = None, H = None):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

    if H is not None:
        corners = np.float32([[0, 0], [w1, 0], [w1, h1], [0, h1]])
        corners = np.int32( cv2.perspectiveTransform(corners.reshape(1, -1, 2), H).reshape(-1, 2) + (w1, 0) )
        cv2.polylines(vis, [corners], True, (255, 255, 255))
    
    if status is None:
        status = np.ones(len(p1), np.bool_)
    green = (0, 255, 0)
    red = (0, 0, 255)
    for (x1, y1), (x2, y2), inlier in zip(np.int32(p1), np.int32(p2), status):
        col = [red, green][inlier]
        if inlier:
            cv2.line(vis, (x1, y1), (x2+w1, y2), col)
            cv2.circle(vis, (x1, y1), 2, col, -1)
            cv2.circle(vis, (x2+w1, y2), 2, col, -1)
        else:
            r = 2
            thickness = 3
            cv2.line(vis, (x1-r, y1-r), (x1+r, y1+r), col, thickness)
            cv2.line(vis, (x1-r, y1+r), (x1+r, y1-r), col, thickness)
            cv2.line(vis, (x2+w1-r, y2-r), (x2+w1+r, y2+r), col, thickness)
            cv2.line(vis, (x2+w1-r, y2+r), (x2+w1+r, y2-r), col, thickness)
    return vis


if __name__ == '__main__':
    import sys

        
    #Create object to read images from camera 0
    cam = cv2.VideoCapture(0)

    #Initialize SURF object
    surf = cv2.SURF(1000)

    #Set desired radius
    rad = 2


            
    while TRUE:

##        #Get image from webcam and convert to greyscale
##        ret, img = cam.read()
##        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##
##        #Detect keypoints and descriptors in greyscale image
##        keypoints, descriptors = surf.detect(gray, None, False)
##
##        #Draw a small red circle with the desired radius
##        #at the (x, y) location for each feature found
##        for kp in keypoints:
##            x = int(kp.pt[0])
##            y = int(kp.pt[1])
##            cv2.circle(img, (x, y), rad, (0, 0, 255))
##
##        #Display colour image with detected features
##        cv2.imshow("features", img)
##
##        #Sleep infinite loop for ~10ms
##        #Exit if user presses <Esc>
##        if cv2.waitKey(10) == 27:
##            break
        
##        ret, img = cam.read()
##        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##        kp1, desc1 = surf.detect(img1, None, False)

        ret, im2 = cam.read()
        im = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
        (kp1, desc1) = surf.detect(im, None, False)
        print desc1
        print kp1
        if desc1:        
            img2 = cv2.imread("D:/new.bmp",0)
            kp2, desc2 = surf.detect(img2, None, False)

            desc1.shape = (-1, surf.descriptorSize())
            desc2.shape = (-1, surf.descriptorSize())

        
            def match_and_draw(match, r_threshold):
                m = match(desc1, desc2, r_threshold)
                matched_p1 = np.array([kp1[i].pt for i, j in m])
                matched_p2 = np.array([kp2[j].pt for i, j in m])
                H, status = cv2.findHomography(matched_p1, matched_p2, cv2.RANSAC, 5.0)
                print '%d / %d  inliers/matched' % (np.sum(status), len(status))

                vis = draw_match(img1, img2, matched_p1, matched_p2, status, H)
                return vis

            print 'flann match:',
            vis_flann = match_and_draw( match_flann, 0.6 ) # flann tends to find more distant second
                                                           # neighbours, so r_threshold is decreased
     
            cv2.imshow('find_obj SURF flann', vis_flann)
            cv2.waitKey()
        
##        blobs = img.invert().findBlobs(minsize=100)
##
##        if blobs:
##            for blob in coins:
                #img.drawRectangle(coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,coin.minRectWidth(),coin.minRectHeight(),Color.BLUE,3)
                    
                
##                if (coin.minRectX()-coin.minRectWidth()/2 > 0.0 and coin.minRectY()-coin.minRectHeight()/2 > 0.0 and coin.minRectWidth() > 0.0 and coin.minRectHeight() > 0.0 ):
##
##                    crop = img.crop(coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,coin.minRectWidth(),coin.minRectHeight())
##                    
##                    empty.dl().blit(crop)                
##                    #empty.show()
##                    #empty = empty.resize(200,200)
##              
##                    
##                    blackblob = empty.binarize()
##                    blackblob = blackblob.invert()
##
##                    
##                    
##                    diff = blackblob - template
##
##                    
##                    
##                    matrix = diff.getNumpy()
##                    mean = matrix.mean()
##                    img.drawText(str("%.2f" % round(mean,2)), coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,fontsize = 32)
##                    
##                    if( mean < 0.75):
##                       img.drawRectangle(coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,coin.minRectWidth(),coin.minRectHeight(),Color.BLUE,3)
                    

                    
                #print(str(coin.minRectX()-coin.minRectWidth()/2))
                #print(str(coin.minRectY()-coin.minRectHeight()/2))
                #print(str(coin.minRectWidth()))
                #print(str(coin.minRectHeight()))
        
       # img.show()
