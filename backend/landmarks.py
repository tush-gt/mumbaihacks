import mediapipe as mp
import cv2
import numpy as np

mp_holistic = mp.solutions.holistic

def extract_lip_motion(video_path):
    cap = cv2.VideoCapture(video_path)
    motion_values = []

    with mp_holistic.Holistic(min_detection_confidence=0.5) as holistic:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            if results.face_landmarks:
                # upper lip index = 13, lower lip index = 14
                lip_up = results.face_landmarks.landmark[13]
                lip_down = results.face_landmarks.landmark[14]

                distance = abs(lip_down.y - lip_up.y)
                motion_values.append(distance)

    cap.release()
    return np.array(motion_values)
