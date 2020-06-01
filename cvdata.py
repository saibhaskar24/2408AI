import cv2
import numpy as np
import  imutils
# Load image, grayscale, and adaptive threshold
image = cv2.imread('screen0.png')
image = cv2.resize(image,(400,900))
image = image[330:680,30:370]
large_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



small_image = cv2.imread('32.png')
small_image= cv2.cvtColor(small_image, cv2.COLOR_BGR2GRAY)
print(small_image.shape , large_image.shape)



method = cv2.TM_SQDIFF_NORMED

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)

cv2.waitKey()

