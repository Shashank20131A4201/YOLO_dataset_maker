import cv2
import os

# Define face detection parameters
face_cascade_path = "haarcascade_frontalface_default.xml"  # Path to your Haar cascade file

def face_detection_and_cropping(student_folder_path):
    """
    Processes images within a student folder:
    - Detects faces using Haar cascade.
    - Crops the detected face and saves it with the original filename.
    - Removes the original image if a face is found.
    """

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    for image_filename in os.listdir(student_folder_path):
        if not image_filename.endswith((".jpg", ".jpeg", ".png")):
            continue  # Skip non-image files

        image_path = os.path.join(student_folder_path, image_filename)
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces with adjusted parameters based on feedback
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),  # Adjust minimum face size as needed
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(faces) == 1:  # Exactly one face detected
            (x, y, w, h) = faces[0]
            cropped_face = img[y:y+h, x:x+w]

            # Save the cropped face with the original filename (replace or remove if needed)
            cv2.imwrite(image_path, cropped_face)

            # Delete the original image (Optional: comment out if desired)
            # os.remove(image_path)
        else:  # No face or multiple faces detected (optional handling)
            print(f"Image '{image_path}' doesn't contain exactly one face.")

# Iterate through student folders and process images
for student_folder in os.listdir(os.getcwd()):
    if os.path.isdir(student_folder):
        face_detection_and_cropping(os.path.join(os.getcwd(), student_folder))

print("Face detection and image processing completed!")
