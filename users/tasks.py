from django.core.mail import send_mail
from kutubxona.celery import app



@app.task()
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        "tempkitob@gmail.com",
        recipient_list
    )