import os.path
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def send_message(service, to, subject, body):
    message = {
        'raw': base64.urlsafe_b64encode(
            f"To: {to}\r\nSubject: {subject}\r\n\r\n{body}".encode()
        ).decode()
    }
    service.users().messages().send(userId='me', body=message).execute()
    print("✅ Email terkirim via OAuth2")

if __name__ == "__main__":
    service = gmail_service()
    to      = input("Email penerima: ").strip()
    subject = input("Subjek: ").strip()
    body    = input("Pesan: ").strip()
    count   = int(input("Kirim berapa kali? "))
    for i in range(1, count+1):
        send_message(service, to, f"[{i}/{count}] {subject}",
                     f"{body}\n\n(Pesan ke-{i} dari {count})")
        
