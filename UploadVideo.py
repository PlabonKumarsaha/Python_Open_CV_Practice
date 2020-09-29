# package for opencv
import cv2

# import video
cap = cv2.VideoCapture("Resrouces/video.mp4")
# as video is a collection of images ...The images must be included in a while loop
while True:
    # success is a boolean that looks for if the upload is successful or not!
    success, img = cap.read()
    cv2.imshow("vid",img)
    # this refers that the video will continue to play until q is pressed!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
