import cv2 as cv

# Read Image
# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0)

vid = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = vid.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray, 125, 175)
    cv.imshow("Video", canny)
    if cv.waitKey(10) & 0xFF == ord("q"):
        break

vid.release()
cv.destroyAllWindows()
