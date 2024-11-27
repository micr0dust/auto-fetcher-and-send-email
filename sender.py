import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os
from dotenv import load_dotenv

load_dotenv()
def send_email(html_content, recipient_email, subject, sender_name):
    sender_email = "hellocycudeliveryservice@gmail.com"
    password = os.getenv("MAIL_PASSWORD")
    
    # Email 內容
    msg = MIMEText(html_content, 'html')
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)


if __name__ == "__main__":
    from recvier import recvier_emails
    html_content = "<p>Hello World</p></br><p>這是一封測試郵件</p>"
    send_email(html_content,recvier_emails[0],"測試郵件","爬蟲通知")