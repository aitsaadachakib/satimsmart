from rest_framework import serializers
from .models import TransactionFormComplainsTypes, TransactionForm, ComplaintFormTypes, ComplaintForm

class TransactionFormComplainsTypesSerializer(serializers.ModelSerializer):
    status=serializers.SerializerMethodField()
    def get_status(self, obj):
        return obj.active
    class Meta:
        model = TransactionFormComplainsTypes
        fields = '__all__'
        read_only_fields = ['id','completed_at','status',"created_at"]
        

class TransactionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionForm
        fields = '__all__'

class ComplaintFormTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintFormTypes
        fields = '__all__'

class ComplaintFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintForm
        fields = '__all__' 