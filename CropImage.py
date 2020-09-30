# package for opencv
import cv2
import numpy as np

# Resizing an image
img = cv2.imread("Resrouces/ironman.jpg")
# print the shape
print(img.shape) # returns height , weight and number of channels(ex for BGR it is 3)

imgResize = cv2.resize(img, (300, 200))

imgcroped = img[0:40, 50:80] # works like a vector 
# cv2.imshow("re size", imgResize)
cv2.imshow("Croped Image", imgcroped)
cv2.waitKey(0)


