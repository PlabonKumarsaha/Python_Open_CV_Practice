# package for opencv
import cv2

# read image from path
# stored the image in 'img'
img = cv2.imread("Resrouces/ironman.jpg")

# Convert to grayScale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# first parameter is window name..second is the image name
cv2.imshow("Gray Image", imgGray)
# must adda delay , otherwise the image gets popped down
cv2.waitKey(0)
