import cv2

cap = cv2.VideoCapture(0)

# add opencv contrib to use Moose object detector
# higher speed
tracker = cv2.TrackerMOSSE_create()
tracker1 = cv2.TrackerCSRT_create() # low speed but high accuracy
success , img = cap.read()
boundingBox = cv2.selectROI("Tracking", img , False)
tracker.init(img, boundingBox) # create a bounding box

def drawBox(img , bbox):
    x, y, w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w,y+h)),(255,0,255),3, 1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)


while True:
    timer = cv2.getTickCount()
    success , img = cap.read()

    # updated bounding box
    success ,boundingBox = tracker.update(img)

    if success:
        drawBox()
    else:
        cv2.putText(img, "Object lost", (75, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    # calculate the FPS
    fps =cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(75,50), cv2.FONT_HERSHEY_COMPLEX,0.7, (0, 0 ,255), 2)
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

