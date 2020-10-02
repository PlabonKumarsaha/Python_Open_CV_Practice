# package for opencv
import cv2
import numpy as np

# create a matix of zeroes ..Zero means black in an image

imgMat = np.zeros((500, 500, 3), dtype=np.uint8)
print(imgMat)

# Converts it to blue
imgMat[:] = 255, 0, 0

print(imgMat)

# Draw a line from the 0,0 to 200,200 ..the line is green bcz RGB.. Thickness is 3 of the line
cv2.line(imgMat, (0, 0), (200, 200), (0, 255, 0), 3)

# draws a red rectangle
cv2.rectangle(imgMat, (0, 0), (150, 250), (0, 0, 255), 2)

# draw a filled rectangle ((left,top),(right,bottom),color ,filling up the rect)
cv2.rectangle(imgMat, (180, 360), (350, 450), (0, 0, 255), cv2.FILLED)

# Circle drawing..first param is the position..2nd is the radius and 3rd is the thickness

cv2.circle(imgMat, (420, 280), 30, (255, 255, 0), 5)

cv2.imshow("Image", imgMat)
cv2.waitKey(0)


# Draw Shapes in Images
