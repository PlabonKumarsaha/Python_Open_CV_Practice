# package for opencv
import cv2
import numpy as np

# create a matix of zeroes ..Zero means black in an image

imgMat = np.zeros((500, 500, 3), dtype=np.uint8)
print(imgMat)

# Converts it to blue
imgMat[:] = 255, 0, 0

print(imgMat)

# Show Text
# image = cv2.putText(image, 'OpenCV', org, font,
#                    fontScale, color, thickness, cv2.LINE_AA)

imgMat = cv2.putText(imgMat, "OpenCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow("Image", imgMat)
cv2.waitKey(0)


# Draw Shapes in Images
