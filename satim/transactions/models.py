from random import choice
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    transactionid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('aborted', 'Aborted'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    montant = models.DecimalField(max_digits=30, decimal_places=2, help_text="Montant of the transaction")
    #TODO add client