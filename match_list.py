import face_recognition
import os

# Load the known image and encoding
known_image_path = "tom.png"
known_image = face_recognition.load_image_file(known_image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]

# Define the folder containing multiple unknown images
unknown_images_folder = "images"

# Initialize a list to store filenames with matches
matching_filenames = []

# Loop through the images in the "unknown_images" folder
for filename in os.listdir(unknown_images_folder):
    unknown_image_path = os.path.join(unknown_images_folder, filename)

    # Load the current unknown image from the folder
    unknown_image = face_recognition.load_image_file(unknown_image_path)

    # Encode all the faces in the current unknown image
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    # Compare the known encoding with all the face encodings in the current unknown image
    for unknown_encoding in unknown_encodings:
        results = face_recognition.compare_faces([known_encoding], unknown_encoding)

        if results[0]:
            matching_filenames.append(filename)
            break  # Break the loop if at least one match is found for this image

if matching_filenames:
    print("Matches found in the following files:")
    for filename in matching_filenames:
        print(filename)
else:
    print("No matches found.")
