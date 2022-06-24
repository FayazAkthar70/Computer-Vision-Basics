import cv2 as cv
import mediapipe as mp
import time
import face_detection_module as fdm

current_time = 0
prev_time = 0
vid = cv.VideoCapture(0)

while True:
    isTrue, img = vid.read()
    face_detector = fdm.faceDetector()
    img = face_detector.find_face(img)
    current_time = time.time()
    fps = str(int(1/(current_time-prev_time)))
    prev_time = current_time
    cv.putText(img, fps, (10,70), cv.FONT_HERSHEY_COMPLEX, 2,(0,0,0), 3)
    
    cv.imshow('video',img)
    if cv.waitKey(10) & 0xFF == ord("q"):   #press q to close video
        break
    
vid.release()
cv.destroyAllWindows()