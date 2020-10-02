# package for opencv
import cv2
import numpy as np

# create a matix of zeroes ..Zero means black in an image

width, height = 250, 350
img = cv2.imread("Resrouces/ironman.jpg")

# cut within some points
pts1 = np.floor32([[111, 219], [287, 188], [154, 482], [352, 440]])

# Point where we want to show the image
pts2 = np.floor32([[0, 0], [width, 0], [0, height], [width, height]])

# Apply the perspective transformation algorithm
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("output", img)
cv2.imshow("output", imgOut)



