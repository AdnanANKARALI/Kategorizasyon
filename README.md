# Görüntü Kalsifikasyon Sınıflandırma Projesi

Bu proje, medikal görüntülerde kalsifikasyon ve kitlenin tespiti ve sınıflandırılması amacıyla geliştirilmiştir. Kullanılan algoritmalar ve model, özellikle YOLO (You Only Look Once) tabanlıdır ve EfficientNet mimarisinden faydalanarak görüntü sınıflandırma görevini yerine getirmektedir. Proje kapsamında, DICOM (DCM) formatındaki tıbbi görüntüler işlenerek uygun formata dönüştürülmekte, ardından model eğitimi ve değerlendirmesi yapılmaktadır.

## Proje Amacı

Bu projenin amacı, medikal görüntülerdeki kalsifikasyon ve kitlelerin doğru ve hızlı bir şekilde tespit edilmesini sağlamaktır. Model, eğitim ve test verileri üzerinde çalıştırılarak doğru tahminler yapabilmekte ve bu tür tespitler için sağlık profesyonellerine yardımcı olabilecek bir çözüm sunmaktadır.

## Dosya ve Kod Açıklamaları

### 1. `dataPrep.py`
Bu dosya, verilerin hazırlanmasından sorumludur. Eğitim ve test verilerinin uygun formatlarda hazırlanması ve sınıflandırma için modelin kullanabileceği şekilde işlenmesi gibi işlemler yapılmaktadır.
- **Fonksiyonlar**: Verilerin sınıflara ayrılması, etiketlerin düzenlenmesi, ve model eğitimi için gerekli verilerin oluşturulması.
- **Amaç**: Eğitim sürecinde kullanılan verilerin doğru bir şekilde hazırlanmasını sağlamak.

### 2. `dcmTopng.py`
Bu dosya, DICOM (DCM) formatındaki tıbbi görüntülerin PNG formatına dönüştürülmesini sağlar.
- **Fonksiyonlar**: Tıbbi görüntülerin dosya yapısına göre okunması, dönüştürülmesi ve ilgili dizinlere kaydedilmesi.
- **Amaç**: Modelin, görüntüleri daha yaygın bir format olan PNG formatında kullanabilmesi için dönüştürme işlemi yapılmaktadır.

### 3. `test.py`
Bu dosya, eğitilmiş modelin test verileri üzerinde çalıştırılarak değerlendirilmesini sağlar.
- **Fonksiyonlar**: Eğitilen modelin test verileri üzerinde tahminler yapması ve sonuçların analiz edilmesi.
- **Amaç**: Modelin performansının değerlendirilmesi ve doğruluk, kayıp gibi metriklerin hesaplanması.

### 4. `train.py`
Bu dosya, modelin eğitim sürecini yürütür. YOLO ve EfficientNet tabanlı model, belirtilen eğitim verileri üzerinde eğitilir.
- **Fonksiyonlar**: Modelin yapılandırılması, hiperparametrelerin ayarlanması ve eğitim sürecinin yürütülmesi.
- **Amaç**: Modelin medikal görüntülerdeki kalsifikasyon ve kitleleri doğru bir şekilde tanıyacak şekilde eğitilmesi.

## Kurulum ve Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki gereksinimlerin kurulması gerekmektedir:

- Python 3.8+
- PyTorch
- OpenCV
- NumPy
- pandas
- albumentations
- YOLOv8 (Ultralytics)
- EfficientNet-PyTorch

Gereksinimleri kurmak için:

```bash
pip install -r requirements.txt
