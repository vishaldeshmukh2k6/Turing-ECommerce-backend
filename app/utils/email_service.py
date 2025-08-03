from flask_mail import Message
from app.extensions import mail
from flask import current_app

def send_email(subject, recipients, body, html=None):
    msg = Message(subject, recipients=recipients, body=body, html=html, sender=current_app.config["MAIL_USERNAME"])
    mail.send(msg)
