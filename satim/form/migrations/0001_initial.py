# Generated by Django 5.2.3 on 2025-06-20 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintFormTypes',
            fields=[
                ('name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionFormComplainsTypes',
            fields=[
                ('name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('family_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=11)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('transactionid', models.CharField(blank=True, max_length=255, null=True)),
                ('complaint', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('comleted', 'comleted'), ('rejected', 'rejected')], default='pending', max_length=255)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('complaint_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='form.complaintformtypes')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain', models.TextField(blank=True, null=True)),
                ('transactionid', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('comleted', 'comleted'), ('rejected', 'rejected')], default='pending', max_length=255)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('complain_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='form.transactionformcomplainstypes')),
            ],
        ),
    ]
