# package for opencv
import cv2
import numpy as np

# read image from path
# stored the image in 'img'
img = cv2.imread("Resrouces/ironman.jpg")
# take kernel with all the values as 1
kernel = np.ones((6, 6), np.ones)

# Convert to gausian blue ..11x11 is k size which must be odd and signifies the density of blurness
imgCanny = cv2.Canny(img,100,100)

# changes thickness in the imgCanny..increasing itteration values will change the dialation
imgDialetion =cv2.dilate(imgCanny,kernel,1)
imgErode =cv2.erode(imgDialetion,kernel,1)

# first parameter is window name..second is the image name
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialetion)
cv2.imshow("Erroson Image", imgErode)

# must adda delay , otherwise the image gets popped down
cv2.waitKey(0)
