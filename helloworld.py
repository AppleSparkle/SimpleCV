from SimpleCV import *

cam = Camera()

template = Image("D:/new.bmp")
template = template.binarize()
template = template.invert()

empty = Image("D:/empty.bmp")


while TRUE:
    
    img = cam.getImage()
    
    coins = img.invert().findBlobs(minsize=100)

    if coins:
        for coin in coins:
            #img.drawRectangle(coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,coin.minRectWidth(),coin.minRectHeight(),Color.BLUE,3)
                
            
            if (coin.minRectX()-coin.minRectWidth()/2 > 0.0 and coin.minRectY()-coin.minRectHeight()/2 > 0.0 and coin.minRectWidth() > 0.0 and coin.minRectHeight() > 0.0 ):

                crop = img.crop(coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,coin.minRectWidth(),coin.minRectHeight())
                
                empty.dl().blit(crop)                
                #empty.show()
                #empty = empty.resize(200,200)
          
                
                blackblob = empty.binarize()
                blackblob = blackblob.invert()

                
                
                diff = blackblob - template

                
                
                matrix = diff.getNumpy()
                mean = matrix.mean()
                img.drawText(str("%.2f" % round(mean,2)), coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,fontsize = 32)
                
                if( mean < 0.75):
                   img.drawRectangle(coin.minRectX()-coin.minRectWidth()/2,coin.minRectY()-coin.minRectHeight()/2,coin.minRectWidth(),coin.minRectHeight(),Color.BLUE,3)
                

                
            #print(str(coin.minRectX()-coin.minRectWidth()/2))
            #print(str(coin.minRectY()-coin.minRectHeight()/2))
            #print(str(coin.minRectWidth()))
            #print(str(coin.minRectHeight()))
    
   # img.show()
