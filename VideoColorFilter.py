import cv2
import numpy as np

def empty(a):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

#HSV
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


#BGR
cv2.createTrackbar("Blue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Blue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Green Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Green Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Red Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Red Max", "TrackBars", 255, 255, empty)


#YCrCb
cv2.createTrackbar("Lum Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Lum Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Cr Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Cr Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Cb Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Cb Max", "TrackBars", 255, 255, empty)


#LAB
cv2.createTrackbar("Light Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Light Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("A Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("A Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("B Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("B Max", "TrackBars", 255, 255, empty)

while True:
    #takes a frame from webcam
    success, frame = cap.read()

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    #convert frame to HSV
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsvFrame, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)



    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break