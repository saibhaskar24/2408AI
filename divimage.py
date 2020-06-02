import cv2
import matplotlib.pyplot as plt
# Load image, grayscale, and adaptive threshold
image = cv2.imread('myimage.png')
image = cv2.resize(image,(350,350))
# i = image[0:30,0:30]
# cv2.imshow("myimage",i8)
plt.imshow(image)
# cv2.imwrite("0.png",i)
# cv2.waitKey()
plt.show()

# print(image.shape)

for i in range(0,350,91):
    for j in range(0,340,91):
        plt.imshow(image[i:80+i,j:80+j])
        plt.show()