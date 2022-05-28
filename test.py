import cv2
import numpy as np




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

# def colorizer(image):
#     output = np.zeros(image.shape)
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             # colors = (int(img[i][j][0]),int(img[i][j][1]),int(img[i][j][2]))
            
#             if img[i][j][0] > img[i][j][1] and img[i][j][2]:
#                 print(type(img[i][j][0]),img[i][j][1],img[i][j][2])
#                 output[i][j][0] = ((img[i][j][0]+img[i][j][1]+img[i][j][2])/3)
#                 print(output[i][j][0])
            #changes reds
            # if colors[0] > colors[1] and colors[2]:
            #     output[i][j][0] = int((colors[0]+colors[1]+colors[2])/3)
            #     output[i][j][1] = 0
            #     output[i][j][2] = 0
            #changes greens
            # if colors[1] > colors[0] and colors[2]:
            #     output[i][j][0] = 0
            #     output[i][j][1] = int((colors[0]+colors[1]+colors[2])/3)
            #     output[i][j][2] = 0
            # #changes blues
            # if colors[2] > colors[1] and colors[0]:
            #     output[i][j][0] = 0
            #     output[i][j][1] = 0
            #     output[i][j][2] = int((colors[0]+colors[1]+colors[2])/3)
            #leaves it alone if none of the above
            # else:
            # output[j][i] = img[j][i]
    # return output

# colorizedimg = colorizer(img)
# cv2.imwrite('colorized.png',colorizedimg)

# print("before:")
# print(img[0][0],img[0][-1])
# print(img[-1][0],img[-1][-1])
# print("after")
# print(colorizedimg[0][0],colorizedimg[0][-1])
# print(colorizedimg[-1][0],colorizedimg[-1][-1])

# print(img[300][300])
# num = (img[300][300][0]+img[300][300][1]+img[300][300][2])/3
# num1 = int(img[300][300][1])
# num2 = int(img[300][300][2])
# num0 = int(img[300][300][0])
# avgnum = int((num0+num1+num2)/3)
# print(avgnum)
# bgr = (int(image[300][300][0]),int(image[300][300][1]),int(image[300][300][2]))
# rgb = (int(img[300][300][0]),int(img[300][300][1]),int(img[300][300][2]))
# # print (bgr,rgb)
# # print(type(bgr),type(rgb))
# rgb1 = (200,5,5)
# if rgb1[0] > rgb1[1] and rgb1[2]:
#     rgb2 = int((rgb1[0]+rgb1[1]+rgb1[2])/3)
#     print (rgb1,rgb2)
# print(img[300][300])
#make a 4 pixel image with orange, blueish, greenish, and grey
#check the datatypes for int back to uint8

#top right, top left, 