from django.db import models, transaction

# Create your models here.

class TransactionFormComplainsTypes(models.Model):
    name=models.CharField(max_length=60,primary_key=True)
    active=models.BooleanField(default=True)

class TransactionForm(models.Model):
    complain_type=models.ForeignKey(TransactionFormComplainsTypes, on_delete=models.SET_NULL,null=True,blank=True)
    complain=models.TextField(null=True,blank=True)
    transactionid=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=255,default='pending',choices=[('pending','pending'),('comleted','comleted'),('rejected','rejected')])
    completed_at=models.DateTimeField(null=True,blank=True)

class ComplaintFormTypes(models.Model):
    name=models.CharField(max_length=60,primary_key=True)
    active=models.BooleanField(default=True)

class ComplaintForm(models.Model):
    name=models.CharField(max_length=60)
    family_name=models.CharField(max_length=60)
    phone_number=models.CharField(max_length=11)
    email=models.EmailField(null=True,blank=True)
    transactionid=models.CharField(max_length=255,null=True,blank=True)
    complaint_type=models.ForeignKey(ComplaintFormTypes, on_delete=models.SET_NULL,null=True,blank=True)
    complaint=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=255,default='pending',choices=[('pending','pending'),('comleted','comleted'),('rejected','rejected')])
    completed_at=models.DateTimeField(null=True,blank=True)


