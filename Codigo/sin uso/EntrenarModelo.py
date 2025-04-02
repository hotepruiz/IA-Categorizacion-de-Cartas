from ultralytics import YOLO
import os
model = YOLO("yolov8n.pt") 

model.train(data="data.yaml", epochs=50, imgsz=640)
