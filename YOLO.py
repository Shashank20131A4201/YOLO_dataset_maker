from ultralytics import YOLO
import os
import cv2
def draw_bbox(frame, boxes, colors):
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Extracting the class label and name
        cls = int(box.cls[0])
        class_name = "Face"

        # Retrieving the color for the class
        color = colors[cls]

        # Drawing the bounding box on the image
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

        # Formatting the confidence level and label text
        conf = math.ceil((box.conf[0] * 100)) / 100
        label = f'{class_name} ({conf}%)'

        # Calculating the size of the label text
        text_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
        # Calculating the coordinates for the background rectangle of the label
        rect_coords = x1 + text_size[0], y1 - text_size[1] - 3

        # Drawing the background rectangle and the label text
        cv2.rectangle(frame, (x1, y1), rect_coords, color, -1, cv2.LINE_AA)
        cv2.putText(frame, label, (x1, y1 - 2), 0, 1, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
    return frame
# sudo apt update
# sudo apt install -y libgl1-mesa-glx libglib2.0-0
model = YOLO('best.pt',verbose=False)
video_folder_path = os.path.join(os.getcwd(), "videos")
for office in os.listdir(video_folder_path):
    office_path = os.path.join(video_folder_path, office)
    for students in os.listdir(office_path):
        student_folder = os.path.join(office_path, students)
        for image_filename in os.listdir(student_folder):
            if not image_filename.endswith((".jpg", ".jpeg", ".png")):
                continue  # Skip non-image file
            image_path = os.path.join(student_folder, image_filename)
            frame = cv2.imread(image_path)
            result = model(frame, conf=0.5)[0]
            boxes = result.boxes
            if boxes==None:
                print("No face")
            box = boxes[0]
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            width = x2 - x1
            height = y2 - y1
            cropped_image = frame[y1:y1+height, x1:x1+width]
            cv2.imwrite(image_path, cropped_image)


