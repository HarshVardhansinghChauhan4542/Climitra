import cv2
import os

# === Parameters ===
video_path = 'region3.mov'     # Path to your input video
output_dir = 'frames4'             # Folder to save frames

# === Create output directory ===
os.makedirs(output_dir, exist_ok=True)

# === Read the video ===
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error opening video file: {video_path}")
    exit()

frame_index = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_filename = os.path.join(output_dir, f"{frame_index}.jpg")
    cv2.imwrite(frame_filename, frame)
    frame_index += 1

cap.release()
print(f"Saved {frame_index} frames to '{output_dir}'")
