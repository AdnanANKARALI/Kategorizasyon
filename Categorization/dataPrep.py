import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Dataset yolunu belirleyelim
dataset_path = '/kaggle/input/kategoridataset/'

# CSV dosyasını yükleyelim
csv_file_path = '/kaggle/input/veriset/veribilgisi.csv'
veri = pd.read_csv(csv_file_path, delimiter=';')

# Dosya uzantılarını .png olarak değiştirelim
veri['DOSYA ADI'] = veri['DOSYA ADI'].apply(lambda x: os.path.splitext(x)[0] + '.png')

# Klasör yapısındaki tüm dosya isimlerini toplayalım
file_paths = []
categories = os.listdir(dataset_path)

for category in categories:
    category_path = os.path.join(dataset_path, category)
    if os.path.isdir(category_path):
        patient_ids = os.listdir(category_path)
        for patient_id in patient_ids:
            patient_path = os.path.join(category_path, patient_id)
            if os.path.isdir(patient_path):
                files = os.listdir(patient_path)
                for file in files:
                    file_paths.append(os.path.join(category, patient_id, file))

# Dosya isimlerini içeren bir DataFrame oluşturalım
files_df = pd.DataFrame(file_paths, columns=['Dosya Yolu'])

# CSV dosyasındaki dosya isimlerini normalize edelim (büyük/küçük harf farkını kaldırmadan)
veri['Dosya Yolu'] = veri.apply(lambda row: os.path.join(row['KATEGORİ'], str(row['HASTA ID']), row['DOSYA ADI']), axis=1)

# Karşılaştırma yapalım ve eşleşen dosyaları bulalım
eslesenler = veri[veri['Dosya Yolu'].isin(files_df['Dosya Yolu'])]

# Eşleşen dosyaları kaydedelim
matching_records_path = '/kaggle/working/matching_records.csv'
eslesenler.to_csv(matching_records_path, index=False)

# Eşleşmeyen dosyaları bulalım
uyusmayanlar = veri[~veri['Dosya Yolu'].isin(files_df['Dosya Yolu'])]

# Eşleşmeyen dosyaların yüzdesini hesaplayalım
total_files = len(veri)
mismatched_files = len(uyusmayanlar)
mismatch_percentage = (mismatched_files / total_files) * 100
print(f"Eşleşmeyen dosyaların yüzdesi: {mismatch_percentage}%")

# Eşleşmeyen dosyaları kontrol edelim
print("Eşleşmeyen dosyalar:")
print(uyusmayanlar)

matching_records_path = '/kaggle/working/matching_records.csv'
eslesenler = pd.read_csv(matching_records_path)

filtered_records = eslesenler[eslesenler['ETİKET ADI'].isin(['Kitle', 'Kalsifikasyon'])]

filtered_records_path = '/kaggle/working/filtered_records.csv'
filtered_records.to_csv(filtered_records_path, index=False)

print(filtered_records.head())