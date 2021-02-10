import cv2
import numpy as np

print("Package imported!")
classFile = 'res/coco.names'
className = []
with open(classFile , 'rt') as f:
    className = f.read().rstrip('\n').split('\n')
    print(className)

modelConfiguration = 'res/yolov3-tiny.cfg'
modelWeight = 'res/yolov3-tiny.weights'

# net = cv2.dnn.readNetFromDarknet(modelConfiguration ,modelWeight)
net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeight)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


image1 = cv2.imread("res/car.jpg")
image1 = cv2.resize(image1, (300, 300))
cv2.imshow("Gray Image", image1)
cv2.waitKey(0)





