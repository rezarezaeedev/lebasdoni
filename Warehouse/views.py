from rest_framework.viewsets import ModelViewSet
from . import models as mymodels
from . import serializers as myserializers

class ProductInfoView(ModelViewSet):
	queryset = mymodels.ProductInfo.objects.all()
	serializer_class = myserializers.ProductInfoSerializer


class ProductView(ModelViewSet):
	queryset = mymodels.Product.objects.all()
	serializer_class = myserializers.ProductSerializer


class CategoryView(ModelViewSet):
	queryset = mymodels.Category.objects.all()
	serializer_class = myserializers.CategorySerializer


class SexView(ModelViewSet):
	queryset = mymodels.Sex.objects.all()
	serializer_class = myserializers.SexSerializer
