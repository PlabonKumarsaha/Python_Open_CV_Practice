# package for opencv
import cv2

# read image from path
# stored the image in 'img'
img = cv2.imread("Resrouces/ironman.jpg")

# Convert to gausian blue ..11x11 is k size which must be odd and signifies the density of blurness
imgCanny = cv2.Canny(img,100,100)
# first parameter is window name..second is the image name
cv2.imshow("Canny Image", imgCanny)
# must adda delay , otherwise the image gets popped down
cv2.waitKey(0)
