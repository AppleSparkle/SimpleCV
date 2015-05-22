from SimpleCV import *

cam = Camera()

while TRUE:
    
    img = cam.getImage()

    img = img.binarize()
    img = img.invert()
    img = img.erode()

    blobs = img.findBlobs(minsize=30)
        
    if blobs:
        blobs.draw()
        for blob in blobs:
            x = blob.coordinates()[0]
            y = blob.coordinates()[1]
            #img.drawCircle
            
            

    img.show()    
    
