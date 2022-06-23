import cv2 as cv

vid = cv.VideoCapture('./Resources/Videos/dog.mp4')


#for video, live video and images
def resize(frame, scale):
    width =  int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    width,height = 1920,1080
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    

#capture method only for live video

while True:
    isTrue,frame = vid.read()
    frame_resize = resize(frame, 1.5)
    
    cv.imshow('Video',frame)
    cv.imshow('Video',frame_resize)
    
    if cv.waitKey(10) & 0xFF == ord('q'):
        break
    
vid.release()
cv.destroyAllWindows()