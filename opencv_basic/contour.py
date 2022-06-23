import cv2 as cv
from cv2 import RETR_LIST
from cv2 import CHAIN_APPROX_NONE
from cv2 import CHAIN_APPROX_SIMPLE
from cv2 import RETR_TREE
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
greyscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.blur(greyscale,(5,5),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175,)


contour, heirarchy = cv.findContours(canny, RETR_TREE, CHAIN_APPROX_SIMPLE)
blank = np.zeros(img.shape, dtype=np.uint8)
cv.drawContours(blank, contour, -1, (0,255,0), 2)
cv.imshow('blank',blank)


contour_none, heirarchy_none = cv.findContours(canny, RETR_LIST, CHAIN_APPROX_NONE)
blank = np.zeros(img.shape, dtype=np.uint8)
cv.drawContours(blank, contour_none, -1, (0,255,0), 2)
cv.imshow('blank_none',blank)

cv.waitKey(0)