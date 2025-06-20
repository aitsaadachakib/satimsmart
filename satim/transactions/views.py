from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
from rest_framework import serializers
from apikeys.authentication import APIKeyAuthentication

# Create your views here.

class TransactionView(APIView):
    authentication_classes = [APIKeyAuthentication]

    def post(self, request, *args, **kwargs):
        user = request.user
        transaction=Transaction(user=user)
        transaction.save()
        return Response({'transaction_id':transaction.transactionid }, status=status.HTTP_200_OK)


