from django.shortcuts import render
from rest_framework.views import APIView
from .models import ImageTransaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ImageTransactionSerializer



class ImageTransactionView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class=ImageTransactionSerializer
    permission_classes = []
    def get(self, request):
        transactions = ImageTransaction.objects.all()
        serializer = ImageTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageTransactionSerializer(data=request.data)
        if serializer.is_valid():
            imagetransaction=serializer.save()
            image_file=imagetransaction.image
            # TODO add model heare
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)