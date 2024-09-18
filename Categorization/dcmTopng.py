import os
import pydicom
from pydicom.pixel_data_handlers.util import apply_modality_lut, apply_voi_lut
from PIL import Image
import numpy as np

def dicom_to_png(dicom_file_path, png_file_path):
    try:
        # DICOM dosyasını oku
        dicom = pydicom.dcmread(dicom_file_path)

        # Pixel verilerini al
        image = dicom.pixel_array

        # LUT (Look-Up Table) uygula
        image = apply_modality_lut(image, dicom)
        image = apply_voi_lut(image, dicom)

        # Normalize et ve 8-bit'e dönüştür
        image = (image - np.min(image)) / (np.max(image) - np.min(image)) * 255.0
        image = np.uint8(image)

        # Görüntüyü PNG formatında kaydet
        image_pil = Image.fromarray(image)
        image_pil.save(png_file_path)
    except Exception as e:
        print(f"Error converting file {dicom_file_path}: {e}")

def convert_specific_folder(src_dir, dest_dir, specific_folder):
    specific_folder_path = os.path.join(src_dir, specific_folder)
    
    for root, dirs, files in os.walk(specific_folder_path):
        for file in files:
            if file.endswith(".dcm"):
                dicom_file_path = os.path.join(root, file)
                
                # Hedef dosya yolunu oluştur
                relative_path = os.path.relpath(root, src_dir)
                output_dir = os.path.join(dest_dir, relative_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                png_file_path = os.path.join(output_dir, file.replace(".dcm", ".png"))
                
                # DICOM'u PNG'ye dönüştür
                dicom_to_png(dicom_file_path, png_file_path)


# Kullanım
src_dir = "/kaggle/input/tekno2/tekno2/Teknofest-2024"
dest_dir = "/kaggle/working/"
specific_folder = "Kategori2Sag"

convert_specific_folder(src_dir, dest_dir, specific_folder)
