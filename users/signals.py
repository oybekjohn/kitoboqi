from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
                "Welcome to Kitob O'qi project!",
                f"Hi { instance.username }, This is test message from our project.",
                "tempkitob@gmail.com",
                [instance.email]
            )