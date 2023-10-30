import cv2

def get_frames(CAPTURE_FILE):
    # load the video
    cap = cv2.VideoCapture(CAPTURE_FILE)
    desired_fps = 10
    cap.set(cv2.CAP_PROP_FPS, desired_fps)

    if not cap.isOpened():
        print("Cannot open video file")
        exit()

    # the number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Devide the video into 100 frames
    step_size = total_frames // 200

    frames_list = []
    frame_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Get the frame every step_size
        if frame_number % step_size == 0:
            frames_list.append(frame)

        frame_number += 1

        # Stop when the list is full
        if len(frames_list) == 200:
            break

    return frames_list, cap
