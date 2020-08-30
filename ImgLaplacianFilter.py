import cv2
import numpy as np

img = cv2.imread('Images\drew_selfie.jpg')
img = cv2.GaussianBlur(img, (3, 3), 0)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
LapImg = cv2.Laplacian(grayImg, cv2.CV_8U, ksize=3, scale=1, delta=0)

cv2.imshow('Laplacian', LapImg)
cv2.waitKey()