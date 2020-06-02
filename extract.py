import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold
image = cv2.imread('screen3.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

i = image[170:210,190:260]
# cv2.imshow("myimage",i)
plt.imshow(i)
cv2.imwrite("256.png",i)
# cv2.waitKey()
plt.show()
