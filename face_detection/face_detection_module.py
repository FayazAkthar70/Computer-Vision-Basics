import cv2 as cv
import mediapipe as mp

class faceDetector():
    def __init__(self, min_detection_confidence=0.5, model_selection=0):
        self.min_confidence = min_detection_confidence
        self. model_selection = model_selection
        
        self.faceMP = mp.solutions.mediapipe.python.solutions.face_detection
        self.face = self.faceMP.FaceDetection(self.min_confidence, self. model_selection)
        self.mpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils

    def find_face(self, img, draw=True, is_score=True):
        imgRGB = cv.cvtColor(img, code=cv.COLOR_BGR2RGB)
        self.results = self.face.process(imgRGB)
        if self.results.detections:
            for detection in self.results.detections:
                bboxC = detection.location_data.relative_bounding_box
                score = str(round(detection.score[0],3))
                ih, iw, ic = img.shape
                bbox = [int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)]
                if draw:
                    cv.rectangle(img, (bbox[0],bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0,155,155), 2)
                if is_score:
                    cv.putText(img, score, (bbox[0],bbox[1]-10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2 )
        return img            
        