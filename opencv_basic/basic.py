import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)

#grayscale
grayscale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('grayscale', grayscale)

#blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT, )
cv.imshow('blur',blur)

#edge detection
canny = cv.Canny(blur, 120, 171)
cv.imshow('canny', canny)

#image dilation
dilated = cv.dilate(canny, (3,3), iterations=2)
cv.imshow('dilated',dilated)

#image erosion
eroded = cv.erode(dilated,(3,3), iterations=2)
cv.imshow('eroded',eroded)

#resize
resize = cv.resize(img, (500,500))
cv.imshow('resize',resize)

#cropping
cropped = img[50:,250:]
cv.imshow('cropped',cropped)
cv.waitKey(0)