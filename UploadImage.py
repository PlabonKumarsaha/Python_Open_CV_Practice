# package for opencv
import cv2
print("Package imported!")

# read image from path
# stored the image in 'img'
img = cv2.imread("Resrouces/ironman.jpg")
# first parameter is window name..second is the image name
cv2.imshow("output",img)
# must adda delay , otherwise the image gets popped down
cv2.waitKey(0)