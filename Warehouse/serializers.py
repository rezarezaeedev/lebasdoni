from rest_framework import serializers
from . import models as mymodels


class SexSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.Sex



class ProductCommentSerializer(serializers.ModelSerializer):
	username = serializers.SerializerMethodField()

	def get_username(self, obj):
		return obj.user.username

	class Meta:
		fields = '__all__'
		model = mymodels.ProductComment


class ProductInfoSerializer(serializers.ModelSerializer):
	def get_category_names(self, obj):
		return map(lambda x:x.name ,obj.category.all())

	def get_sex_string(self, obj):
		return str(obj.sex)

	def get_likes(self, obj):
		return obj.like_set.all().count()

	def get_comments(self, obj):
		result = ProductCommentSerializer(obj.comment_set.filter(active=1).order_by('-created_at')[:5], many=True,)
		return result.data

	def get_available_in_warehouse(self, obj):
		return obj.product_set.all().count()

		
	category_names = serializers.SerializerMethodField()
	sex_string = serializers.SerializerMethodField()
	likes = serializers.SerializerMethodField()
	comments = serializers.SerializerMethodField()
	available_in_warehouse = serializers.SerializerMethodField()

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


