import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/lady.jpg")
cv.imshow("lady", img)

blur = cv.blur(img, (3, 3))
cv.imshow("blur", blur)

gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("gauss", gauss)

median = cv.medianBlur(img, 3)
cv.imshow("median", median)

bilateral = cv.bilateralFilter(img, 20, 100, 100)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)
