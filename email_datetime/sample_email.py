import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime_basics import datetime

smtp_server = "smtp.gmail.com"
port = 465
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
password = "your_app_password"

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = f"Python test sent at {current_time}"

body = f"Hello! This email was automatically generated and sent on {current_time}."
message.attach(MIMEText(body, "plain"))

try:
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Something went wrong: {e}")