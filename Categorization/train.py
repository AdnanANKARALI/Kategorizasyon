import os
os.environ['WANDB_MODE'] = 'disabled'

from ultralytics import YOLO

# YOLOv8 modelini yükleme
model = YOLO('./input/yolov8s/yolov8s.pt').to("cuda")  # Pretrained YOLOv8 modelini kullanarak

# Eğitim dosyasın0ı hazırlama
data_yaml = f"""
train: {yolo_dataset_path}/train/images
val: {yolo_dataset_path}/val/images

nc: 2
names: ['Kitle', 'Kalsifikasyon']
"""

with open('./working/yolo_dataset/data.yaml', 'w') as f:
    f.write(data_yaml)

# Modeli eğitme
model.train(data='./working/yolo_dataset/data.yaml', epochs=505, imgsz=640, workers=8)