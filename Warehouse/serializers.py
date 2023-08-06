from rest_framework import serializers
from . import models as mymodels


class SexSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.Sex


class ProductInfoSerializer(serializers.ModelSerializer):
	def get_category_names(self, obj):
		return map(lambda x:x.name ,obj.category.all())

	def get_sex_string(self, obj):
		return str(obj.sex)
		
	category_names = serializers.SerializerMethodField()
	sex_string = serializers.SerializerMethodField()

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


class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.Like


class ProductCommentSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.ProductComment

