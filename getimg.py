from SimpleCV import *

cam = Camera()
filename = "D:/test.bmp"

while TRUE:
    img = cam.getImage() 
    img.save(filename)
    img.show()

