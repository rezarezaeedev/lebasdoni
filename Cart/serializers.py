from rest_framework import serializers
from . import models as mymodels


class CartItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = mymodels.CartItem
		fields = '__all__'

	product_info_string = serializers.ReadOnlyField(source='product.product_info.__str__')



class CartSerializer(serializers.ModelSerializer):
	items = serializers.SerializerMethodField()
	username=serializers.SerializerMethodField()

	def get_username(self, obj):
		return obj.user.username

	def get_items(self, obj):
		returnx =  CartItemSerializer(mymodels.CartItem.objects.filter(cart=obj), many=1).data
		print(returnx)
		return returnx

	class Meta:
		model = mymodels.Cart
		fields = '__all__'
