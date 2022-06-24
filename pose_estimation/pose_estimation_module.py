import cv2 as cv
import mediapipe as mp
import time

class Pose_detector():
    def __init__(self, mode=False, complex=1, smooth=True, segment=False, smooth_segment=True, detection_conf=0.5, track_conf=0.5):
        self.mode = mode
        self.complex = complex
        self.smooth = smooth
        self.segment = segment
        self.smooth_segment = smooth_segment
        self.detection_conf = detection_conf
        self.track_conf = track_conf
        
        self.mpPose = mp.solutions.mediapipe.python.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complex, self.smooth, self.segment, self.smooth_segment, self.detection_conf, self.track_conf)
        self.mpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils
    
    def find_pose(self, img):
        imgRGB = cv.cvtColor(img, code=cv.COLOR_BGR2RGB)
        self.result = self.pose.process(imgRGB)
        
        if self.result.pose_landmarks:
            self.mpDraw.draw_landmarks(img, self.result.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def find_position(self, img, draw=True):
        pose_landmarks = []
        if self.result.pose_landmarks:
            for id,landmark in enumerate(self.result.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(landmark.x*w), int(landmark.y*h)
                print([id,cx,cy])
                pose_landmarks.append([id,cx,cy])
                if draw and id == 14:   #right elbow id
                    cv.circle(img, (cx,cy), 10, (0,255,0), -1)
        return pose_landmarks
    
