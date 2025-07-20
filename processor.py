import cv2
import pytesseract
from datetime import datetime
import numpy as np

def detect_face(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    if img is None:
        return False
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    return len(faces) > 0

def extract_metadata(image_path):
    img = cv2.imread(image_path)
    if img is None:
        # Handle invalid image gracefully
        return {
            "filename": image_path.split("/")[-1],
            "timestamp": None,
            "avg_color": [0, 0, 0],
            "faces": 0,
            "face_detected": False,
            "text": ""
        }

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    timestamp = datetime.now().isoformat()
    colors = cv2.mean(img)[:3]
    text = pytesseract.image_to_string(gray).strip()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces_rects = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    faces_count = len(faces_rects)
    face_detected = faces_count > 0

    return {
        "filename": image_path.split("/")[-1],
        "timestamp": timestamp,
        "avg_color": [int(c) for c in colors],
        "faces": faces_count,
        "face_detected": face_detected,
        "text": text
    }
