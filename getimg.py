from SimpleCV import *

cam = Camera()
filename = "D:/test.bmp"

while display.isNotDone():    
    display.checkEvents()#check for mouse clicks
    
    img = cam.getImage()
    if display.mouseLeft: # click the mouse to read  
        img.save(filename)
        print "Saved."
        
    img.show()

