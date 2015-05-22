from SimpleCV import *
from socket import socket

cam = Camera()
disp = Display()

new_img = Image("D:/new.bmp")


sock = socket()
sock.connect(('127.0.0.1', 5000))
sock.send('Hallo')

while disp.isNotDone():
        img = cam.getImage() #grab a frame
        img = img.binarize()
        holes = img.findBlobs()
        
        if holes:
                img.drawCircle((holes[-1].x,holes[-1].y),10,color=Color.RED)
                img.drawCircle((holes[-1].centroid()),10,color=Color.BLUE)
                #img.dl().circle(holes[-1].centroid() , 10, Color.RED)
                #x = holes[-1].minX()
                #sock.send(str(x))
                #holes.draw()
                img.drawText(str(holes[-1].x))
                img.drawText(str(holes[-1].y))
                #holes[-1].blobMask().show()

                img_out = holes[-1].getFullMask()
                img_out = img_out - new_img.invert()
                img_out.show()
                
        #win = img.show()
        
        if disp.mouseLeft:                
                win.quit()
                break
                

        
        
        
