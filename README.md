# 📊 Madduck Data Case Study – App Store Lead Filtering Script  

💡 **App Store verilerini filtrele • 🎯 Deal List hariç tut • ⏳ Son güncellemeleri kontrol et • 👨‍💻 Tekilleştirilmiş geliştirici bazlı uygulama seç**  

---

## 📌 Proje Hakkında  

Bu proje, App Store’dan alınan uygulama verilerini **CRM sistemine uygun hale getirmek** için geliştirilmiş bir Python scripti içerir.  
Script, verilen App List ve Deal List üzerinden uygulamaları çekerek **filtreleme kurallarına göre eleme yapar** ve sonuçları CSV dosyasına kaydeder.  

> ✅ App Store API’den metadata çekme  
> ✅ Deal List’teki uygulamaları hariç tutma  
> ✅ Release Date ve Last Update Date filtreleri  
> ✅ Her geliştiriciden yalnızca 1 uygulama seçme (tekilleştirme)  
> ✅ Yeniden kullanılabilir terminal scripti (`argparse` ile)  

---

## 🔧 Kullanılan Teknolojiler  

| Teknoloji/Kütüphane | Açıklama |
|---------------------|----------|
| 🐍 Python           | Geliştirme dili |
| 📑 Pandas           | Veri işleme |
| 🌍 Requests         | App Store API çağrıları |
| ⏱️ Datetime         | Tarih filtreleme |
| 🖥️ Argparse         | Terminal parametre desteği |

---

## 📁 Klasör / Dosya Yapısı  
📦 madduck_data_case
┣ 📓 script.py # Ana Python scripti
┣ 📊 M
┣ 📑 filtered_leads.csv # Çıktı (filtrelenmiş uygulamalar)


---

## 🚀 Kurulum ve Çalıştırma  

🔹 Gerekli paketleri yükleyin:  
```bash
pip install pandas requests openpyxl

🔹 Script’i terminalden şu şekilde çalıştırabilirsiniz:
python script.py --input "Madduck Data Case Study Data Files.xlsx" --output "filtered_leads.csv"

Parametreler

--input→ Excel dosya yolu

--output → Çıktı CSV dosyası (varsayılan: filtered_leads.csv)

Örnekler:
python script.py --input "Madduck Data Case Study Data.xlsx" --output "sonuc.csv"
python script.py --input "baska_dosya.xlsx" --output "filtered.csv"




