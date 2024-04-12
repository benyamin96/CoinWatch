import smtplib
from config import TO, EMAIL_PROVIDER, SMTP_SERVER_EMAIL, SMTP_SERVER_PASSWORD, SMTP_PORT
from email.mime.text import MIMEText


def send_smtp_email(body, subject=None):
    msg = MIMEText(body)
    msg['subject'] = subject if subject else 'CoinWatch Notification'
    msg['from'] = 'from@domain.com'
    msg['to'] = TO

    try:
        with smtplib.SMTP(msg[EMAIL_PROVIDER], SMTP_PORT) as mail_server:
            mail_server.login(SMTP_SERVER_EMAIL, SMTP_SERVER_PASSWORD)
            mail_server.sendmail(msg['from'], msg['to'], msg.as_string())
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
