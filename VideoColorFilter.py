import cv2
import numpy as np

def empty(a):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("TrackBarsBGR")
cv2.resizeWindow("TrackBarsBGR", 640, 240)

cv2.namedWindow("TrackBarsHSV")
cv2.resizeWindow("TrackBarsHSV", 640, 240)

cv2.namedWindow("TrackBarsYCrCb")
cv2.resizeWindow("TrackBarsYCrCb", 640, 240)

cv2.namedWindow("TrackBarsLAB")
cv2.resizeWindow("TrackBarsLAB", 640, 240)

#BGR
cv2.createTrackbar("Blue Min", "TrackBarsBGR", 0, 255, empty)
cv2.createTrackbar("Blue Max", "TrackBarsBGR", 255, 255, empty)
cv2.createTrackbar("Green Min", "TrackBarsBGR", 0, 255, empty)
cv2.createTrackbar("Green Max", "TrackBarsBGR", 255, 255, empty)
cv2.createTrackbar("Red Min", "TrackBarsBGR", 0, 255, empty)
cv2.createTrackbar("Red Max", "TrackBarsBGR", 255, 255, empty)


#HSV
cv2.createTrackbar("Hue Min", "TrackBarsHSV", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBarsHSV", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBarsHSV", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBarsHSV", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBarsHSV", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBarsHSV", 255, 255, empty)


#YCrCb
cv2.createTrackbar("Lum Min", "TrackBarsYCrCb", 0, 255, empty)
cv2.createTrackbar("Lum Max", "TrackBarsYCrCb", 255, 255, empty)
cv2.createTrackbar("Cr Min", "TrackBarsYCrCb", 1, 255, empty)
cv2.createTrackbar("Cr Max", "TrackBarsYCrCb", 255, 255, empty)
cv2.createTrackbar("Cb Min", "TrackBarsYCrCb", 1, 255, empty)
cv2.createTrackbar("Cb Max", "TrackBarsYCrCb", 255, 255, empty)


#LAB
cv2.createTrackbar("Light Min", "TrackBarsLAB", 0, 255, empty)
cv2.createTrackbar("Light Max", "TrackBarsLAB", 255, 255, empty)
cv2.createTrackbar("A Min", "TrackBarsLAB", 1, 225, empty)
cv2.createTrackbar("A Max", "TrackBarsLAB", 255, 255, empty)
cv2.createTrackbar("B Min", "TrackBarsLAB", 1, 255, empty)
cv2.createTrackbar("B Max", "TrackBarsLAB", 255, 255, empty)



while True:
    #takes a frame from webcam
    success, frame = cap.read()

    b_min = cv2.getTrackbarPos("Blue Min", "TrackBarsBGR")
    b_max = cv2.getTrackbarPos("Blue Max", "TrackBarsBGR")
    g_min = cv2.getTrackbarPos("Green Min", "TrackBarsBGR")
    g_max = cv2.getTrackbarPos("Green Max", "TrackBarsBGR")
    r_min = cv2.getTrackbarPos("Red Min", "TrackBarsBGR")
    r_max = cv2.getTrackbarPos("Red Max", "TrackBarsBGR")

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBarsHSV")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBarsHSV")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBarsHSV")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBarsHSV")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBarsHSV")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBarsHSV")

    Lum_min = cv2.getTrackbarPos("Lum Min", "TrackBarsYCrCb")
    Lum_max = cv2.getTrackbarPos("Lum Max", "TrackBarsYCrCb")
    Cr_min = cv2.getTrackbarPos("Cr Min", "TrackBarsYCrCb")
    Cr_max = cv2.getTrackbarPos("Cr Max", "TrackBarsYCrCb")
    Cb_min = cv2.getTrackbarPos("Cb Min", "TrackBarsYCrCb")
    Cb_max = cv2.getTrackbarPos("Cb Max", "TrackBarsYCrCb")

    L_min = cv2.getTrackbarPos("Light Min", "TrackBarsLAB")
    L_max = cv2.getTrackbarPos("Light Max", "TrackBarsLAB")
    A_min = cv2.getTrackbarPos("A Min", "TrackBarsLAB")
    A_max = cv2.getTrackbarPos("A Max", "TrackBarsLAB")
    B_min = cv2.getTrackbarPos("B Min", "TrackBarsLAB")
    B_max = cv2.getTrackbarPos("B Max", "TrackBarsLAB")

    bgrlower = np.array([b_min, g_min, r_min])
    bgrupper = np.array([b_max, g_max, r_max])
    bgrmask = cv2.inRange(frame, bgrlower, bgrupper)
    bgrresult = cv2.bitwise_and(frame, frame, mask=bgrmask)


    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsvlower = np.array([h_min, s_min, v_min])
    hsvupper = np.array([h_max, s_max, v_max])
    hsvmask = cv2.inRange(hsvFrame, hsvlower, hsvupper)
    hsvresult = cv2.bitwise_and(frame, frame, mask=hsvmask)


    ycrcbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    ycrcblower = np.array([Lum_min, Cr_min, Cb_min])
    ycrcbupper = np.array([Lum_max, Cr_max, Cb_max])
    ycrcbmask = cv2.inRange(ycrcbFrame, ycrcblower, ycrcbupper)
    ycrcbresult = cv2.bitwise_and(frame, frame, mask=ycrcbmask)


    labFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    lablower = np.array([L_min, A_min, B_min])
    labupper = np.array([L_max, A_max, B_max])
    labmask = cv2.inRange(labFrame, lablower, labupper)
    labresult = cv2.bitwise_and(frame, frame, mask=labmask)

    cv2.imshow('Original', frame)
    cv2.imshow('BGRResult', bgrresult)
    cv2.imshow('HSVResult', hsvresult)
    cv2.imshow('YCRCBResult', ycrcbresult)
    cv2.imshow('LABResult', labresult)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break