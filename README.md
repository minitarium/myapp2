# MyApp2
Prototype project WhatsApp Web AI Reply menggunakan Python, Selenium, dan Gemini AI.

## ✨ Fitur
- Balasan otomatis di WhatsApp Web dengan AI Gemini.
- Simulasi mengetik manusiawi (huruf per huruf).
- Penyimpanan riwayat chat per kontak.
- Saklar pause/resume bot.

## ⚙️ Instalasi
1. Clone repo:
   ```bash
   git clone https://github.com/minitarium/myapp2.git
   cd myapp2
2. Buat virtual environment (opsional):
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

4. Install dependencies
pip install -r requirements.txt

## 🚀 Menjalankan Bot
1. Jalankan script:
   ```bash
   python app.py
2. Scan QR Code WhatsApp Web di browser.
3. Bot akan otomatis membaca dan membalas pesan.
   
### Konfigurasi
```markdown
## 🔑 Konfigurasi
- API Key Gemini disimpan di variabel `API_KEYS` dalam `app.py`.
- Riwayat chat tersimpan di folder `D:/ChatHistory`.
- Nama bot bisa diubah di variabel `BOT_NAME`.

# Lisensi (opsional)
## 📄 Lisensi
Project ini dibuat untuk keperluan belajar dan prototyping.

