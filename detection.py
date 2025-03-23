import cv2
import torch
from ultralytics import YOLO

# Load the trained model
model = YOLO("models/yolov8n.pt")  # Use trained model instead of yolov8n.pt

# Function to detect items in an image
def detect_items(image_path):
    image = cv2.imread(image_path)
    results = model(image)
    detected_items = set()

    for r in results:
        for box in r.boxes:
            detected_items.add(model.names[int(box.cls[0])])  # Extract detected object names
    
    return list(detected_items)

# Function to compare before & after images
def find_missing_items(before_image_path, after_image_path):
    before_items = detect_items(before_image_path)
    after_items = detect_items(after_image_path)
    missing_items = set(before_items) - set(after_items)
    return missing_items

# Paths to images
before_image = "D:\\srm\\ML\\yolo\\before.png" 
after_image = "D:\\srm\ML\\yolo\\after.jpeg" 

# Find missing items
missing_items = find_missing_items(before_image, after_image)

# Output result
print("Missing Items:", missing_items)

