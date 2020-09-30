# package for opencv
import cv2

# read image from path
# stored the image in 'img'
img = cv2.imread("Resrouces/ironman.jpg")

# Convert to gausian blue ..11x11 is k size which must be odd and signifies the density of blurness
imgBlur = cv2.GaussianBlur(img, (11, 11), 2)
# first parameter is window name..second is the image name
cv2.imshow("Gray Image", imgBlur)
# must adda delay , otherwise the image gets popped down
cv2.waitKey(0)
