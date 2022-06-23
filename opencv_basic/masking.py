import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/lady.jpg")

blank = np.zeros(img.shape[:2], dtype="uint8")

circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow("filter", blank)

filtered = cv.bitwise_and(img, img, mask=circle)
cv.imshow("filter_img", filtered)

cv.waitKey(0)
