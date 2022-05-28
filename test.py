from turtle import color
import cv2
import numpy as np
import random


image = cv2.imread('testcolors2.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
colorizedimg = img.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

noiseyimg = np.zeros(image.shape,np.uint8) #.zeros makes an array of 0s, i think .uint8 assigns 8bits per value
for i in range(img.shape[1]):
    for j in range(img.shape[0]):
        rdn = random.random()
        if rdn < .35:
            noiseyimg[i][j] = (255,0,0) #blue
        elif rdn > .65:
            noiseyimg[i][j] = (0,255,0) #green
        else:
            noiseyimg[i][j] = (0,0,255) #red


for i in range(colorizedimg.shape[1]):
    for j in range(colorizedimg.shape[0]):
        if noiseyimg[i][j][0] > noiseyimg[i][j][1] and noiseyimg[i][j][0] > noiseyimg[i][j][2]:
            colorizedimg[i][j][0] = gray[i][j]
            colorizedimg[i][j][1] = 0
            colorizedimg[i][j][2] = 0
        if noiseyimg[i][j][1] > noiseyimg[i][j][0] and noiseyimg[i][j][1] > noiseyimg[i][j][2]:
            colorizedimg[i][j][1] = gray[i][j]
            colorizedimg[i][j][0] = 0
            colorizedimg[i][j][2] = 0
        if noiseyimg[i][j][2] > noiseyimg[i][j][0] and noiseyimg[i][j][2] > noiseyimg[i][j][1]:
            colorizedimg[i][j][2] = gray[i][j]
            colorizedimg[i][j][0] = 0
            colorizedimg[i][j][1] = 0
       
        
colorizedimg = cv2.cvtColor(colorizedimg, cv2.COLOR_BGR2RGB)
cv2.imwrite('colorizedimg.png',colorizedimg)


        
#     thres = 1 - prob 
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = (255,0,0) #blue
#             elif rdn > thres:
#                 output[i][j] = (0,255,0) #green
#             else:
#                 output[i][j] = (0,0,255) #red

# def colorize(img):
#     output = np.zeros(image.shape,np.uint8)
#     print(output)
#     #convert image to three channels
#     red = bgr[:,:,0]
#     green = bgr[:,:,1]
#     blue = bgr[:,:,2]
#     for i in range(len(red)):


#         #convert image to grayscale, use that value for luminance
#     return output
# colorized = colorize(img)
# colorizedimg = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
# cv2.imwrite('colorizedimg.png',colorizedimg)



# def sp_noise(image,prob):
#     '''
#     Add salt and pepper noise to image
#     prob: Probability of the noise
#     '''
#     output = np.zeros(image.shape,np.uint8) #.zeros makes an array of 0s, i think .uint8 assigns 8bits per value
#     thres = 1 - prob 
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = (255,0,0) #blue
#             elif rdn > thres:
#                 output[i][j] = (0,255,0) #green
#             else:
#                 output[i][j] = (0,0,255) #red
#     return output
# image = cv2.imread('gray.png',cv2.IMREAD_COLOR) # Only for grayscale image(?)
# noise_img = sp_noise(image,.35) #add a slider to second argument
# cv2.imwrite('sp_noise.png', noise_img)
# image = cv2.imread('testcolors.png',cv2.IMREAD_COLOR)
# img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

