import cv2
import numpy as np

def empty(a):
    pass


cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    
    frame = cv2.GaussianBlur(frame, (3, 3), 0)

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gradient_x = cv2.Sobel(grayFrame, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0)
    gradient_y = cv2.Sobel(grayFrame, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0)

    abs_gradient_x = cv2.convertScaleAbs(gradient_x)
    abs_gradient_y = cv2.convertScaleAbs(gradient_y)

    gradientFrame = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

    cv2.imshow('Sobel', gradientFrame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break