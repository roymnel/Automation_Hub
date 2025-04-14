# send_email.py
# Reusable module for sending receipts with attachments via email

import smtplib
from email.message import EmailMessage
from .email_config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_receipt(recipient, subject, body, attachment_path):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach PDF receipt
    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = f.name.split("/")[-1]
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    # Send via SMTP
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"[✓] Receipt sent to {recipient}")
