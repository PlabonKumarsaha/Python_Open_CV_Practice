# https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html

# histogram is a graph or plot, which gives you an overall idea about the intensity distribution of an image. It is a plot with pixel values (ranging from 0 to 255, not always) in 
# X-axis and corresponding number of pixels in the image on Y-axis

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

dark_horse = cv2.imread("img/horse.jgp")
rainBow = cv2.imread("img/rainbow.jgp")
bricks = cv2.imread("img/bricks.jgp")

show_horse = cv2.cvtColor(dark_horse,cv2.BGR2RGB) # convert for mat plot lib
show_rainbow = cv2.cvtColor(rainBow,cv2.BGR2RGB) # convert for mat plot lib
show_bricks = cv2.cvtColor(bricks,cv2.BGR2RGB) # convert for mat plot lib


#open bgr.here channel[0] is blue index 
hist_values = cv2.calcHist([show_bricks], channel[0] , mask = None , histSize=[256], ranges =[0,256])

plt.plot(hist_values) # the histrogramic value of the image will be displayed ranging on various values 

img = bricks

color = ('b' , 'g' , 'r')

for i, col in enumerate(color):
hisr = cv2.calcHist([img],[i], None , [256], [0,256])
plt.plot(hisr,color = col) # plots RGB seperately
plt.xlim([0,256]) # if the image is too large

plt.title('Histrogram for blue bricks')

