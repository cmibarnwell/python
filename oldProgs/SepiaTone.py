#Sepia Tone Program written by Caleb Barnwell
#Computer Science, 11-22-15

import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        R= p.getRed()
        G=p.getGreen()
        B=p.getBlue()
        
        newRed = (R *0.393 + G * 0.769 + B * 0.189)
        newGreen = (R * 0.349 + G * 0.686 + B * 0.168)
        newBlue = (R * 0.272 + G * 0.534 + B * 0.131)

        newpixel = image.Pixel(newRed, newGreen, newBlue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()
