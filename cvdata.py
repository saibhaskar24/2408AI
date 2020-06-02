import cv2
import numpy as np

# Load image, grayscale, and adaptive threshold
image = cv2.imread('screen3.png')
# image = cv2.resize(image,(400,900))
image = image
large_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

small_image = cv2.imread('data/256.png')
small_image= cv2.cvtColor(small_image, cv2.COLOR_BGR2GRAY)
w, h = small_image.shape[::-1]

res = cv2.matchTemplate(large_image,small_image,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('Image', large_image)
cv2.waitKey()

