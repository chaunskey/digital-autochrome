import numpy as np
import random
import cv2
from PIL import Image, ImageOps, ImageColor

#---import the source image
srcimg = Image.open('cat.jpg')
# print(srcimg.size) #shows the dimensions of srcimg as a tuple

# noisey = Image.new(mode = "RGB", size = (srcimg.size), color = (100, 100, 100))
# print(type(noisey))
# gray = Image.open('gray.jpg')
# noisey = gray.effect_noise((gray.size),.5)
# noisey.save('noisey2.jpg')


#---make noisey image file, same size as the source file
img  = Image.new( mode = "RGB", size = (srcimg.size), color = (100, 100, 100) )
img.save('gray.jpg')
def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
image = cv2.imread('gray.jpg',0) # Only for grayscale image
noise_img = sp_noise(image,.6)
cv2.imwrite('sp_noise.jpg', noise_img)

#---add green noise, then blue noise, then red noise


#---parse thru pixels, and assign each pixel the RGB value of according to which color the autochrome noise is
    #luminance value?

#---add a function for changing the histogram?

