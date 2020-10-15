import cv2
import numpy as np
import matplotlib.pyplot as plt

print("done")

def canny(image):
    # kenny edge detection - boundary of an object..it aactually difefrmciates sharm changes in color
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)  # convert to grayscale
    gausianBlur = cv2.GaussianBlur(gray, (5, 5), 0)  # reduce noise from the image
    canny = cv2.Canny(gausianBlur, 50, 150)  # outlines the strongest gradient from the images
    return canny

def region_of_interest(image):
    # differnciate the region of interest
    height = image.shape[0]
    polygons =np.array([[(200, height), (1100, height), (550, 250)]]) # make it an array bcz there will be several polygoons
    mask = np.zeros_like(image) # make a copy of the image but make all the pixels black
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask) # applying bit wise and in masked and input image will show the region of interest

    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

            return line_image;




image = cv2.imread("Resources/lane.png")

lane_image = np.copy(image)
canny = canny(lane_image)
cropedImage = region_of_interest(canny) # shows the region of interest
minLinelength=40
maxLineGap=5
lines = cv2.HoughLines(cropedImage, 2, np.pi/180, 100, np.array([]), minLinelength, maxLineGap)
line_image = display_lines(lane_image, lines)
comb_image =cv2.addWeighted(lane_image, 0.8, line_image, 1, 1) # adding the detected line in the picture
cv2.imshow("Output", comb_image)
cv2.waitKey(0)

