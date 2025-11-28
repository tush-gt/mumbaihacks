import cv2
import mediapipe as mp
import numpy as np

mp_holistic = mp.solutions.holistic

def extract_lip_motion(video_path):
    cap = cv2.VideoCapture(video_path)
    motion_values = []

    if not cap.isOpened():
        print("Error opening video file")
        return np.array([])

    with mp_holistic.Holistic(
        static_image_mode=False,
        model_complexity=1,
        enable_segmentation=False,
        refine_face_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as holistic:

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Reduce size for faster processing
            frame = cv2.resize(frame, (640, 360))
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = holistic.process(frame_rgb)

            # Check if face landmarks detected
            if results.face_landmarks:
                landmarks = results.face_landmarks.landmark

                # MediaPipe lip indices
                upper_lip_idx = 13
                lower_lip_idx = 14

                lip_up = landmarks[upper_lip_idx]
                lip_down = landmarks[lower_lip_idx]

                # Distance calculation (normalized because values range 0–1)
                distance = abs(lip_down.y - lip_up.y)

                # Append motion value
                motion_values.append(distance)

    cap.release()
    motion_values = np.array(motion_values)

    return motion_values
