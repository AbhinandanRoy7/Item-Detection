from ultralytics import YOLO

# Load pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # Using YOLOv8 nano model as base
dataset = fiftyone.zoo.load_zoo_dataset("open-images-v6", split="validation")
# Train model on custom dataset
model.train(dataset, epochs=50, imgsz=640)
