import gradio as gr
import cv2
import os
from YOLO import crop_images

def submit_form(firstname, lastname, designation, office, video):
    if not video:
        return "Error: Please record a video."

    # Define base directory for videos (adjust the path as needed)
    base_dir = "videos"

    # Create folder for current submission (office_name)
    office_dir = os.path.join(base_dir, office.lower())
    os.makedirs(office_dir, exist_ok=True)

    # Create folder for individual frames (firstname_lastname)
    individual_dir = os.path.join(office_dir, f"{firstname.lower()}_{lastname.lower()}")
    os.makedirs(individual_dir, exist_ok=True)

    # Open the video capture object
    cap = cv2.VideoCapture(video)

    # Define video processing logic
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Generate filename with frame number
        filename = f"{firstname}_{lastname}_{designation}_{cap.get(cv2.CAP_PROP_POS_FRAMES)}.jpg"
        filepath = os.path.join(individual_dir, filename)

        # Save the frame
        cv2.imwrite(filepath, frame)

    cap.release()

    return f"Video submitted and processed. Frames saved to '{individual_dir}'"

# Create the Gradio interface
video_input = gr.Video(label="Record Video", source="webcam")
interface = gr.Interface(
    fn=submit_form,
    inputs=[gr.Textbox(label="Firstname"), gr.Textbox(label="Lastname"), gr.Textbox(label="Designation"), gr.Textbox(label="Office"), video_input],
    outputs="text",
    title="Form Submission with Video Recording",
    description="Fill in the form and record a video.",
    theme="compact"
)

# Launch the interface
interface.launch()
crop_images()
