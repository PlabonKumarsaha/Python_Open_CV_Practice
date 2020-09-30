# package for opencv
import cv2

# import video
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# change brigtness
cap.set(10, 100)
# as video is a collection of images ...The images must be included in a while loop
while True:
    # success is a boolean that looks for if the upload is successful or not!
    success, img = cap.read()
    cv2.imshow("web_camera",img)
    # this refers that the video will continue to play until q is pressed!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
