from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework import mixins
from . import models as mymodels
from . import serializers as myserializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response


class ProductInfoView(ModelViewSet):
	queryset = mymodels.ProductInfo.objects.all()
	serializer_class = myserializers.ProductInfoSerializer
	filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
	filterset_fields = ('sex', 'size', 'category')
	search_fields = ['name', 'color', 'category__name', 'sex__sex_persian', 'sex__sex']
	ordering_fields = ['price', 'size', 'name']
	ordering = ['-like', '-comment_set__rate']

class ProductView(ModelViewSet):
	queryset = mymodels.Product.objects.all()
	serializer_class = myserializers.ProductSerializer


class CategoryView(ModelViewSet):
	queryset = mymodels.Category.objects.all()
	serializer_class = myserializers.CategorySerializer


class SexView(ReadOnlyModelViewSet):
	queryset = mymodels.Sex.objects.all()
	serializer_class = myserializers.SexSerializer


class LikeView(CreateAPIView, UpdateAPIView,):
	queryset = mymodels.Like.objects.all()
	serializer_class = myserializers.LikeSerializer


class ProductCommentView(CreateAPIView):
	queryset = mymodels.ProductComment.objects.all()
	serializer_class = myserializers.ProductCommentSerializer
	
	 
