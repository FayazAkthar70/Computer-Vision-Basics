import cv2 as cv
import time
import pose_estimation_module as pem

def main():
    current_time = 0
    prev_time = 0
    detector = pem.Pose_detector()
    vid = cv.VideoCapture('Videos/video3.mp4')
    
    while True:
        isTrue, img = vid.read()
        img = detector.find_pose(img)
        pose_landmarks = detector.find_position(img)
        
        current_time = time.time()
        fps = str(int(1/(current_time-prev_time)))
        prev_time = current_time
        cv.putText(img, fps, (10,70), cv.FONT_HERSHEY_COMPLEX, 2,(0,0,0), 3)
        
        cv.imshow('video',img)
        if cv.waitKey(10) & 0xFF == ord("q"):
            break
        
    vid.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()