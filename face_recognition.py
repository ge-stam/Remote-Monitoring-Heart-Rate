import sys
import cv2
from videoprops import get_video_properties
import numpy as np

############################################################################
### prints characteristics of video input
############################################################################
def read_video(path):

    props = get_video_properties(path)
    print(f''' Codec: {props['codec_name']}
    Resolution: {props['width']}×{props['height']}
    Aspect ratio: {props['display_aspect_ratio']}
    Frame rate: {props['avg_frame_rate']} '''.encode("utf-8")) # aproximatelly 30 frames per second

#############################################################################
### get video as input and get a rectangle with the face detected
#############################################################################
### based on
### https://github.com/rohintangirala/eulerian-remote-heartrate-detection/blob/master/preprocessing.py
############################################################################

    cascPath = r"C:\Users\stamo\Desktop\Webcam-Face-Detect-master\Webcam-Face-Detect-master\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

# Read in and simultaneously preprocess video
    cap = cv2.VideoCapture(path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    video_frames = []
    face_rects = ()

    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        roi_frame = img

        # Detect face
        if len(video_frames) == 0:
            face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)

        # Select ROI
        if len(face_rects) > 0:
            for (x, y, w, h) in face_rects:
                roi_frame = img[y:y + h, x:x + w]

            if roi_frame.size != img.size:
                roi_frame = cv2.resize(roi_frame, (500, 500))
                frame = np.ndarray(shape=roi_frame.shape, dtype="float")
                frame[:] = roi_frame * (1. / 255)
                video_frames.append(frame)

    frame_ct = len(video_frames)
    cap.release()

    return video_frames, frame_ct, fps
