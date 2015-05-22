from SimpleCV import *
import zbar

cam = Camera()
display = Display((800,600))

while display.isNotDone():    
    display.checkEvents()#check for mouse clicks
    
    img = cam.getImage()
    #img = img.invert()
    #img = img.binarize()
    
    if display.mouseLeft: # click the mouse to read   
        #img = cam.getImage()
        #configure zbar
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        raw = img.getPIL().convert('L').tostring()
        width = img.width
        height = img.height
        # wrap image data
        image = zbar.Image(width, height, 'Y800', raw)
        # scan the image for barcodes
        scanner.scan(image)
        barcode = None
        # extract results
        print "Found:"
        for symbol in image:            
            # do something useful with results
            barcode = symbol            
            f = Barcode(img, barcode)
            f.draw()
            data = str(f.data)
            print data
            
    img.show()    
    
