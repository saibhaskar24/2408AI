import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold
image = cv2.imread('live.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



i = image[300:330,197:234]
# cv2.imshow("myimage",i)
plt.imshow(i)
cv2.imwrite("16.png",i)
# cv2.waitKey()
plt.show()
