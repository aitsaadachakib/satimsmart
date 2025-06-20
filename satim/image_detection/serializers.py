from rest_framework import serializers
from .models import ImageTransaction

class ImageTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTransaction
        fields = '__all__' 
        read_only_fields = ['id','added_at',]