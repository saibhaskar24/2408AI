import cv2
import  numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


def scanimage(image):
    image = cv2.resize(image,(350,350))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # plt.imshow(image)
    # plt.imshow(cv2.imread('myimage.png'))

    plt.show()

    l = ['2.png','4.png','8.png','32.png','64.png','128.png']

    def mydata(imgg):
        val = 0
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
            if(len(loc[0]) > 0):
                val = int(i[:-4])
                # cv2.imshow('Image', img)
                # print("found: ",i)
                # cv2.waitKey()
        return val




    array = []

    for i in range(0,350,91):
        row = []
        for j in range(0,340,91):
            img = image[i:80+i,j:80+j]
            # cv2.imshow("Split", img)
            # cv2.waitKey()
            row.append(mydata(img))
        array.append(row)
    return array

# image = cv2.imread('myimage.png')

# myarray = scanimage(image)