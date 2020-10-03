# package for opencv
import cv2
import numpy as np


def getContours(img):
    # Rete _external is best for outer corner
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # seperate the elements
        area = cv2.contourArea(cnt)
        # seperatly print the are of the elements
        print(area)
        # give minimum threashold to avoid error
        if area>200:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
        peri = cv2.arcLength(cnt, True)
        print(peri)
        # get the corner points
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        print(approx)
        # create a bounding box for the shapes
        objCorner =len(approx)
        x, y ,w ,h =cv2.boundingRect(approx)

        if objCorner == 3:
            objText = "Triangle"
        else: objText = "none"
# draws the rectangle
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),3)
        # puts the text in the position
        cv2.putText(imgContour, objText, ((x+w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)


# Find about shapes from the images

path = 'Resrouces/sp.png'
img = cv2.imread(path)

# create a copy of the image to pass it to the getContour function
imgContour = img.copy()

# Convert into gray scale and bit of bluer(to prevent distracting element from the image)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imgGray, (7, 7), 2)

# Find the edges from the image .USe canny function
imgCanny = cv2.Canny(imageBlur, 50, 50)

getContours(imgCanny)

cv2.imshow("Original", img)
cv2.imshow("Blur", imageBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("contours", imgContour)


cv2.waitKey(0)



