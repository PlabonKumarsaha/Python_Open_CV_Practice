# package for opencv
import cv2
import numpy as np

# Resizing an image
img = cv2.imread("Resrouces/ironman.jpg")
# print the shape
print(img.shape) # returns height , weight and number of channels(ex for BGR it is 3)

imgResize = cv2.resize(img, (300, 200))
print(img.shape)
cv2.imshow("re size",imgResize)
cv2.waitKey(0)
