from django.contrib.auth.models import AbstractUser

from django.db import models



class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="default_profile_pic.png")



# # email yuborish uchun ishlatsa bo'ladi
#     def save():
#         super().save()