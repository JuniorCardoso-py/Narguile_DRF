from rest_framework import viewsets

from narguile.models import Category, Product
from narguile.serializers import CategorySerializer, ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
