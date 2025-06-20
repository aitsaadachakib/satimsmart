from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import TransactionFormComplainsTypes, TransactionForm, ComplaintFormTypes, ComplaintForm
from .serializers import (
    TransactionFormComplainsTypesSerializer,
    TransactionFormSerializer,
    ComplaintFormTypesSerializer,
    ComplaintFormSerializer
)

# Create your views here.

# class TransactionFormComplainsTypesViewSet(mixins.ListModelMixin,
#                                            mixins.CreateModelMixin,
#                                            mixins.RetrieveModelMixin,
#                                            mixins.UpdateModelMixin,
#                                            viewsets.GenericViewSet):
#     queryset = TransactionFormComplainsTypes.objects.all()
#     authentication_classes = [IsAuthenticated]
#     serializer_class = TransactionFormComplainsTypesSerializer

class TransactionFormViewSet(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    queryset = TransactionForm.objects.all().order_by('-created_at')
    serializer_class = TransactionFormSerializer

# class ComplaintFormTypesViewSet(mixins.ListModelMixin,
#                                 mixins.CreateModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 mixins.UpdateModelMixin,
#                                 viewsets.GenericViewSet):
#     queryset = ComplaintFormTypes.objects.all()
#     authentication_classes = [IsAuthenticated]
#     serializer_class = ComplaintFormTypesSerializer

class ComplaintFormViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    queryset = ComplaintForm.objects.all().order_by('-created_at')
    serializer_class = ComplaintFormSerializer
