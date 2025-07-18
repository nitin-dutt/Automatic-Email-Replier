import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from app.config import GMAIL_TOKEN, USER_EMAIL

creds= Credentials(token= GMAIL_TOKEN)
gmail_service = build('gmail','v1',credentials=creds)

def fetch_unread_emails():
    results = gmail_service.users().message().list(userId='me',lablelIds=['INBOX'],q='is:unread').execute()
    messages = results.get('messages',[])
    emails=[]
    for msg in messages:
        txt= gmail_service.users().messages().get(userId='me',id=msg['id'],format='full').execute()
        payload= txt['payload']
        headers= payload['headers']
        subject= next((h['value'] for h in headers if h['name']=='Subject'),'')
        sender= next((h['value']for h in headers if h['name']=='From'),'')
        body= base64.urlsafe_b64decode(payload['body'].get('data','')).decode('utf-8',errors='ignore')
        emails.append({'id':msg['id'],'sender':sender,'subject':subject,'body':body})
    return emails 

def send_email(to,subject,body):
    from email.mime.text import MIMEText
    import base64
    message=MIMEText(body)
    message['to']=to
    message['subject']= subject
    raw = base64.urlsafe_b64decode(message.as_bytes()).decode()
    gmail_service.users().messages().send(userId='me',body={'raw':raw}).execute()
    