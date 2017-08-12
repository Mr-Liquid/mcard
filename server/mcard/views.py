from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product , Location ,Family ,Transaction
from .serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    """
        List all products, or create a new product.
    """
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
        Retrieve, update or delete a product instance.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def family_list(request):
    """
        List all families.
    """
    if request.method == 'GET':
        family = Family.objects.all()
        serializer = FamilySerializer(family, context={'request': request}, many=True)
        return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def family_detail(request,):

# class family_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer
#
# class location_list(generics.ListCreateAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#
# class location_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Location.objects.all()
#     serializer_class =  LocationSerializer
#
# class transaction_list(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#
# class transaction_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class =  TransactionSerializer