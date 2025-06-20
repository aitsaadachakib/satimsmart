from django.db import models
from transactions.models import Transaction

# Create your models here.
class ImageTransaction(models.Model):
    image = models.ImageField(upload_to='images/')
    added_at = models.DateTimeField(auto_now_add=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='image_transactions')

    def __str__(self):
        return self.image.name