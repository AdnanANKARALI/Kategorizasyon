from ultralytics import YOLO
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import pandas as pd
import os

# Eğitilen modeli yükleme
model = YOLO('./working/runs/detect/train4/weights/best.pt')  # Eğitimden sonra kaydedilen model yolunu kullanın

# Test verisini içeren klasör yolu
test_images_path = './working/yolo_dataset/val/images'

# Tahmin yapma
results = model.predict(source=test_images_path, imgsz=640)

def plot_image_with_boxes(img_path, boxes, labels, scores):
    # Resmi yükle
    img = Image.open(img_path)
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    
    # Bounding box'ları çizme
    ax = plt.gca()
    for box, label, score in zip(boxes, labels, scores):
        x1, y1, x2, y2 = box
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        plt.text(x1, y1, f'{model.names[int(label)]} {score:.2f}', color='white', fontsize=12, bbox=dict(facecolor='red', alpha=0.5))

    plt.axis('off')
    plt.show()

# Tahmin edilen bounding box'ları çizdirme
for result in results:
    img_path = result.path
    boxes = result.boxes.xyxy.cpu().numpy()  # Bounding box koordinatları
    labels = result.boxes.cls.cpu().numpy()  # Sınıf etiketleri
    scores = result.boxes.conf.cpu().numpy()  # Güven skorları

    plot_image_with_boxes(img_path, boxes, "labels", scores)
