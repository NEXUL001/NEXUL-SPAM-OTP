import smtplib
from email.message import EmailMessage
import getpass

# === INPUT DARI USER ===
sender_email   = input("Email pengirim: ").strip()
password       = getpass.getpass("Password / App Password: ")
receiver_email = input("Email penerima: ").strip()
subject        = input("Subjek: ").strip()
body           = input("Isi pesan: ").strip()

while True:
    try:
        count = int(input("Mau kirim berapa kali? (angka): "))
        if count <= 0:
            raise ValueError
        break
    except ValueError:
        print("Harus angka positif!")

# === KIRIM EMAIL ===
sent = 0
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        for i in range(1, count + 1):
            msg = EmailMessage()
            msg["From"]    = sender_email
            msg["To"]      = receiver_email
            msg["Subject"] = f"[{i}/{count}] {subject}"
            msg.set_content(f"{body}\n\n(Pesan ke-{i} dari {count})")
            server.send_message(msg)
            sent += 1
            print(f"✅ Pesan ke-{i} terkirim")
except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")

# === RANGKUMAN ===
print("\n========== RANGKUMAN ==========")
print(f"Dari      : {sender_email}")
print(f"Kepada    : {receiver_email}")
print(f"Subjek    : {subject}")
print(f"Isi pesan : {body}")
print(f"Total     : {sent} pesan berhasil dikirim")
