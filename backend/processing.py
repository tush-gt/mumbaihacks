import requests
import cv2
import os

def download_video(video_url, save_path="downloaded_video.mp4"):
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        return save_path
    else:
        raise Exception("Failed to download video from Cloudinary")


def extract_frames(video_path, frames_dir="data/frames"):
    os.makedirs(frames_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(frames_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        frame_count += 1
        if frame_count >= 200:  # limit for hackathon speed
            break

    cap.release()
    return frame_count
