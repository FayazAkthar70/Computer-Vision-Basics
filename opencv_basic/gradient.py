import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

# soble gradient
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_and(sobel_x, sobel_y)
cv.imshow("soble_combined", sobel_combined)

# canny
canny = cv.Canny(gray, 125, 175)
cv.imshow("canny", canny)
cv.waitKey(0)
