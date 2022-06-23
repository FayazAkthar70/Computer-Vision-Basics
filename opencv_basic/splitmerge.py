import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/lady.jpg")
cv.imshow("lady", img)

b, g, r = cv.split(img)
cv.imshow("blue", b)
cv.imshow("red", r)
cv.imshow("green", g)

merged = cv.merge([b, g, r])
cv.imshow("merged", merged)

blank = np.zeros(b.shape, dtype=np.uint8)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

cv.waitKey(0)
