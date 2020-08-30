import cv2
import numpy as np

def empty(a):
    pass

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Lapframe = cv2.Laplacian(grayframe, cv2.CV_8U, ksize=3, scale=1, delta=0)


    cv2.imshow('Laplacian', Lapframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break