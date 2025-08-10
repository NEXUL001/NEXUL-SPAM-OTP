import requests
import time
import random

# ======= KONFIGURASI =======
API_KEY = "re_RJg6fun8_6zSurQw7aqLMhkA7uLqwjyhJ"  # Ganti dengan API key Resend kamu
EMAIL_FROM = "nexul4you@gmail.com"  # Email pengirim (harus terverifikasi di Resend)
SUBJECT = "Tes Kirim Email via Resend API"
HTML_MESSAGE = """
<h2>Halo!</h2>
<p>Ini pesan tes dari Python & Resend API.</p>
"""
FILE_TARGET = "target.txt"  # File .txt berisi daftar email
JEDA_MIN = 2  # Jeda minimal antar kirim (detik)
JEDA_MAX = 5  # Jeda maksimal antar kirim (detik)
# ===========================

url = "https://api.resend.com/emails"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Baca daftar email dari file
try:
    with open(FILE_TARGET, "r") as f:
        daftar_email = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"❌ File {FILE_TARGET} tidak ditemukan!")
    exit()

print(f"📧 Total email yang akan dikirim: {len(daftar_email)}\n")

# Kirim email satu per satu
for i, email_tujuan in enumerate(daftar_email, start=1):
    data = {
        "from": EMAIL_FROM,
        "to": [email_tujuan],
        "subject": SUBJECT,
        "html": HTML_MESSAGE
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"[{i}/{len(daftar_email)}] ✅ Email terkirim ke {email_tujuan}")
    else:
        print(f"[{i}/{len(daftar_email)}] ❌ Gagal ke {email_tujuan} - {response.status_code} {response.text}")

    # Jeda random untuk aman dari limit
    jeda = random.randint(JEDA_MIN, JEDA_MAX)
    time.sleep(jeda)
