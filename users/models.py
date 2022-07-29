from pyexpat import model
from django.contrib.auth.models import AbstractUser

from django.db import models



class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="profile_default_pic.jpg")