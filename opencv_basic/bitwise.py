import cv2 as cv
import numpy as np

blank = np.zeros((400, 400, 3), dtype="uint8")
rectangle = cv.rectangle(
    blank.copy(), (30, 30), (370, 370), (0, 255, 0), thickness=cv.FILLED
)
circle = cv.circle(blank.copy(), (200, 200), 200, (0, 255, 0), thickness=-1)
cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow("bitwise_and", bitwise_and)

bitwise_or = cv.bitwise_or(circle, rectangle)
cv.imshow("bitwise_or", bitwise_or)

bitwise_xor = cv.bitwise_xor(circle, rectangle)
cv.imshow("bitwise_xor", bitwise_xor)

bitwise_not = cv.bitwise_not(circle)
cv.imshow("bitwise_not", bitwise_not)

cv.waitKey(0)
