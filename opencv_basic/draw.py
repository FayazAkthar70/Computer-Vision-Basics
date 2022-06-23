import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

#draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)

#draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[0]//2, (0,255,0), thickness=-1)

#write text
cv. putText(blank, 'hello world', (100,250), cv.FONT_HERSHEY_COMPLEX, 1, (32,3,153), 2)

cv.imshow('Blank',blank)
cv.waitKey(0)