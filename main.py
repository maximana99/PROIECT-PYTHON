import numpy as np
import cv2 as cv

image = cv.imread('lena.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

img = np.array(image)
height = image.shape[0]
width = image.shape[1]

kernel= np.array([[-1, -1, -1],[-1, 8, -1], [-1, -1, -1]])
#print(kernel)
m= kernel.shape[0]//2
w=h=3
conv= np.zeros(image.shape)
for i in range(m,height-m):
    for j in range(m, width-m):
        s=0
        for k in range(h):
            for l in range(w):
                s=s+img[i-m+k][j-m+l]*kernel[k][l]

        conv[i][j]=s

#print(img)
cv.imshow('img', conv)
cv.waitKey()
#cv.destroyAllWindows()