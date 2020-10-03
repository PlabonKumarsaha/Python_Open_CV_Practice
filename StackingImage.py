# package for opencv
import cv2
import numpy as np

# create a matix of zeroes ..Zero means black in an image

img = cv2.imread("Resrouces/ironman.jpg")

# Adding multiple pics together

# Horizontal stack
hor = np.hstack((img, img))
cv2.imshow("Output",hor)

# Vertical stack
varstack = np.vstack((img, img))
cv2.imshow("Output",varstack)
cv2.waitKey(0)





