import cv2
import numpy as np

img = cv2.imread('Images\drew_selfie.jpg')
img = cv2.GaussianBlur(img, (3, 3), 0)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gradient_x = cv2.Sobel(grayImg, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0)
gradient_y = cv2.Sobel(grayImg, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0)

abs_gradient_x = cv2.convertScaleAbs(gradient_x)
abs_gradient_y = cv2.convertScaleAbs(gradient_y)

gradientImg = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

cv2.imshow('Sobel', gradientImg)
cv2.waitKey()