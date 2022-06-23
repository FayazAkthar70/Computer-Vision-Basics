from asyncio import current_task
import cv2 as cv
from cv2 import COLOR_BGR2RGB
import mediapipe as mp
import time

mpHands = mp.solutions.mediapipe.python.solutions.hands
mpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils
hands = mpHands.Hands()

vid = cv.VideoCapture(0)
current_time = 0
prev_time = 0

while True:
    isTrue, img = vid.read()
    imgRGB = cv.cvtColor(img, code=COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            for id, landmark in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(w*landmark.x), int(h*landmark.y)
                if (id == 4 or id == 8):    # id for thumb and index tip
                    cv.circle(img, (cx, cy), 10, (0,0,0), -1)
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
            
    current_time = time.time()
    fps = str(int(1/(current_time-prev_time)))
    prev_time = current_time
    cv.putText(img, fps, (10,70), cv.FONT_HERSHEY_COMPLEX, 2,(0,0,0), 3)
    cv.imshow('video',img)
    
    if cv.waitKey(10) & 0xFF == ord("q"):
        break
    
vid.release()
cv.destroyAllWindows()