import numpy as np
import random
import cv2
from PIL import Image, ImageOps, ImageColor

#---import the source image
srcimg = Image.open('cat.jpg')
# print(srcimg.size) #shows the dimensions of srcimg as a tuple


#---make noisey image file, same size as the source file

#use cv2.imread to read the image 
#i dont think i need to use pillow at all?
img  = Image.new( mode = "RGB", size = (srcimg.size), color = (100, 100, 100) )
img.save('gray.png') #png is better than jpg because it doesnt mash the pixels up
def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8) #.zeros makes an array of 0s, i think .uint8 assigns 8bits per value
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = (255,0,0) #blue
            elif rdn > thres:
                output[i][j] = (0,255,0) #green
            else:
                output[i][j] = (0,0,255) #red
    return output
image = cv2.imread('gray.png',cv2.IMREAD_COLOR) # Only for grayscale image(?)
noise_img = sp_noise(image,.35) #add a slider to second argument
cv2.imwrite('sp_noise.png', noise_img)

#take original RGB value, subtract/add channel value from/with avg of other two

#---add green noise, then blue noise, then red noise


#---parse thru pixels, and assign each pixel the RGB value of according to which color the autochrome noise is
    #luminance value?

#---add a function for changing the histogram?

