import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Resources/Photos/cat.jpg")

grayscale = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", grayscale)

histogram = cv.calcHist([grayscale], [0], mask=None, histSize=[256], ranges=[0, 256])

plt.figure()
plt.title("color intensity histogram")
plt.xlabel("color intensity")
plt.ylabel("color frequency")
plt.plot(histogram)
plt.xlim([0, 255])
plt.show()

cv.waitKey(0)
