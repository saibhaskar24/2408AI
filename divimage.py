import cv2
import  numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
# Load image, grayscale, and adaptive threshold
image = cv2.imread('myimage.png')
image = cv2.resize(image,(350,350))
# i = image[0:30,0:30]
# cv2.imshow("myimage",i8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(image)

# cv2.imwrite("0.png",i)
# cv2.waitKey()
plt.show()

cv2.imshow("32",cv2.imread(f'data/32.png'))
cv2.waitKey()
# print(image.shape)


l = ['2.png','4.png','8.png','32.png','64.png','128.png']
def mydata(imgg):
    for i in l:
        img = deepcopy(imgg)
        checkimg = cv2.imread(f'data/{i}')
        checkimg= cv2.cvtColor(checkimg, cv2.COLOR_BGR2GRAY)
        w, h = checkimg.shape[::-1]

        res = cv2.matchTemplate(img,checkimg,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        # print(i,loc)
        if(len(loc[0]) > 0):
            cv2.imshow('Image', img)
            print("found: ",i)
            cv2.waitKey()



# mydata(image[280:340,273:353])
# cv2.imwrite("32.png",image[280:340,273:353])

for i in range(0,350,91):
    for j in range(0,340,91):
        # print(i,i+80,j,j+8)
        img = image[i:80+i,j:80+j]
        # plt.imshow(img)
        mydata(img)
        # plt.show()