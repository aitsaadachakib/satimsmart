from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Role(models.Model):
    class Rolechoices(models.TextChoices):
        ADMIN = 'admin'
        USER = 'user'
    role = models.CharField(max_length=255, choices=Rolechoices.choices)
    user=models.OneToOneField(User, related_name='role', on_delete=models.CASCADE)

    def __str__(self):
        return self.role