# package for opencv
import cv2

# import video
frameWidth = 640
frameHeght = 480

cap = cv2.VideoCapture(1)
cap.set(3,frameWidth)
cap.set(4,frameHeght)
# change brigtness
cap.set(10, 130)
# as video is a collection of images ...The images must be included in a while loop
while True:
    # success is a boolean that looks for if the upload is successful or not!
    success, img = cap.read()
    cv2.imshow("web_camera",img)
    # this refers that the video will continue to play until q is pressed!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
