# package for opencv
import cv2
import numpy as np



# Face Detection using Viola & Jones - real time face detection
# To do this we must collect a lot of positive and negative faces(any thing but faces)
# The process is to train  XML file  with these positive and negative images
# there are various open CV cascade to identify eye ,fullbody ,frontalFace

#import the cascade
faceCascade = cv2.CascadeClassifier("Resroices/haarCasacade_file.xml")

path = 'Resrouces/sp.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+2,y+h),(255,0,0),2)





