from django.db import models
from django.contrib.auth.models import User
import secrets

class APIKey(models.Model):
    user = models.ForeignKey(User, related_name='api_keys', on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.key} ({'active' if self.is_active else 'inactive'})"
