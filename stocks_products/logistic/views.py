
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView




class WelcomeView(APIView):
    def get(self, request):
        return Response("Приветствую!")



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

 


class StockViewSet(ModelViewSet):
      queryset = Stock.objects.all()
      
#     queryset = Stock.objects.prefetch_related('positions__product')
      serializer_class = StockSerializer
      ordering_fields = ['id']
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['positions', 'id', 'product']
