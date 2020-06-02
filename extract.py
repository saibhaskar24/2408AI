import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold
image = cv2.imread('myimage.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

i = image[290:330,273:330]
# cv2.imshow("myimage",i)
plt.imshow(i)
cv2.imwrite("32.png",i)
# cv2.waitKey()
plt.show()
