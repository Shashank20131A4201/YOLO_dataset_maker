from ultralytics import YOLO
# Load a model
model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='/workspace/YOLO_dataset_maker/dataset/', epochs=5, imgsz=640)