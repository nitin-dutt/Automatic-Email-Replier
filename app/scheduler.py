from app.email_handler import fetch_unread_emails, send_email
from app.agent_intent import classify_intent
from app.agent_responder import generate_reply
from app.logger import log_email

def run_scheduler():
    print("[RUNNING] Checking for new mails...")
    emails= fetch_unread_emails()
    for email in emails:
        intent = classify_intent(email['body'])
        sender_name= email['sender'].split('<')[0].strip()
        reply= generate_reply(intent, sender_name)
        if reply:
            send_email(email['sender',f"Re: {email['subject']}",reply])
            log_email(email['sender'],email['subject'], intent,"Replied")
        else:
            log_email(email['sender'],email['subject'],intent,"Ignored")
    print(f"[DONE] Processed {len(emails)} emails.")
            