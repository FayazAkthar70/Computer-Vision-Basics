import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Resources/Photos/lady.jpg")


greyscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
cv.imshow("img", img)
cv.imshow("hsv-bgr", hsv_bgr)
cv.imshow("img_convert", lab)
cv.waitKey(0)
