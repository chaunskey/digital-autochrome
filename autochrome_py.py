import numpy as np
import random
import cv2

#---import the source image and convert it from BGR to RGB
image = cv2.imread('cat.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#---make greyscale version of image for avg'd lumen data
colorizedimg = img.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#make np array to create RGB noise
noiseyimg = np.zeros(image.shape,np.uint8) 
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        rdn = random.random()
        if rdn < .35:
            noiseyimg[i][j] = (255,0,0) #blue
        elif rdn > .65:
            noiseyimg[i][j] = (0,255,0) #green
        else:
            noiseyimg[i][j] = (0,0,255) #red

#convert each pixel to noisey image with lumen data from grayscale image
for i in range(colorizedimg.shape[0]):
    for j in range(colorizedimg.shape[1]):
        if noiseyimg[i][j][0] > noiseyimg[i][j][1] and noiseyimg[i][j][0] > noiseyimg[i][j][2]:
            #red channel
            colorizedimg[i][j][0] = gray[i][j]
            colorizedimg[i][j][1] = 0
            colorizedimg[i][j][2] = 0
        if noiseyimg[i][j][1] > noiseyimg[i][j][0] and noiseyimg[i][j][1] > noiseyimg[i][j][2]:
            #green channel
            colorizedimg[i][j][1] = gray[i][j]
            colorizedimg[i][j][0] = 0
            colorizedimg[i][j][2] = 0
        if noiseyimg[i][j][2] > noiseyimg[i][j][0] and noiseyimg[i][j][2] > noiseyimg[i][j][1]:
            #blue channel
            colorizedimg[i][j][2] = gray[i][j]
            colorizedimg[i][j][0] = 0
            colorizedimg[i][j][1] = 0
#need to preserve color data, not just lumen data    

#convert the output to RGB and write the file
colorizedimg = cv2.cvtColor(colorizedimg, cv2.COLOR_BGR2RGB)
cv2.imwrite('colorizedimg.png',colorizedimg)

#---add a function for changing the histogram?

