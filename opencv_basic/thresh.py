import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# simple thresholding
threshold, bin_img = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("bin img", bin_img)
print(threshold)

# adaptive thresholding
adaptive_threshold = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 4
)  # threshold type can be ADAPTIVE_THRESH_GAUSSIAN_C or ADAPTIVE_THRESH_MEAN
cv.imshow("adaptive threshold", adaptive_threshold)
cv.waitKey(0)
