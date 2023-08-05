from rest_framework import serializers
from . import models as mymodels


class SexSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.Sex


class ProductInfoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.ProductInfo


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.Product


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.Category

