import cv2
import face_recognition
import numpy as np

import os 

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the full file paths to your images
image1_path = os.path.join(current_directory, "tom.png")
image2_path = os.path.join(current_directory, "tom1.png")

# Load your images
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Step 3: Convert to grayscale for face detection
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Step 4: Face Detection
# Replace the dlib face detector with OpenCV's face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces1 = face_cascade.detectMultiScale(gray1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
faces2 = face_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Step 5: Check if exactly one face is detected in each image
if len(faces1) == 1 and len(faces2) == 1:
    # Step 6: Face Encoding
    encoding1 = face_recognition.face_encodings(image1, faces1)[0]
    encoding2 = face_recognition.face_encodings(image2, faces2)[0]

    # Step 7: Face Matching
    distance = np.linalg.norm(encoding1 - encoding2)
    threshold = 0.6  # Adjust as needed

    if distance < threshold:
        print("These are the same person.")
    else:
        print("These are different persons.")
else:
    print("One or both images contain zero or multiple faces. Cannot proceed.")