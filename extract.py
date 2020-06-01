import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold
image = cv2.imread('myimage.png')

i8 = image[300:330,280:320]
# cv2.imshow("myimage",i8)
plt.imshow(i8)
cv2.imwrite("32.png",i8)
# cv2.waitKey()
plt.show()