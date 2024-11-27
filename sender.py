import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()
def send_email(html_content, recipient_email, subject="新通知"):
    sender_email = "hellocycudeliveryservice@gmail.com"
    password = os.getenv("MAIL_PASSWORD")
    
    # Email 內容
    msg = MIMEText(html_content, 'html')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)


if __name__ == "__main__":
    html_content = "<p>Hello World</p></br><p>這是一封測試郵件</p>"
    send_email(html_content,"william920107@gmail.com")