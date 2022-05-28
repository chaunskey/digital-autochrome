import cv2
import numpy as np


#img.shape is a 40x40 array with 3 color channels (0,1,2)

image = cv2.imread('testcolors.png')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
grayscale = cv2.imwrite('grayscale.png',img[:,:,0])
print(img[:,:,0][0][0] > img[:,:,1][0][0])

def colorize(img):
    output = np.zeros(image.shape,np.uint8)
    #convert image to three channels
    red = img[:,:,0][0]
    green = img[:,:,1][0]
    blue = img[:,:,2][0]
    for i in range(len(red)):
        #find out which channel in each pixel is strongest and make the other 2 channels 0
        if red[i] > green[i] and blue[i]:
            output[:,:,0][i] = red[i]
            output[:,:,1][i] = 0
            output[:,:,2][i] = 0

        #convert image to grayscale, use that value for luminance
    return output
colorizedimg = colorize(img)
cv2.imwrite('colorizedimg.png',colorizedimg)



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

