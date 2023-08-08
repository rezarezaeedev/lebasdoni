from rest_framework import serializers
from . import models as mymodels
from Warehouse.models import Product


class CartItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = mymodels.CartItem
		fields = '__all__'

	product_info_string = serializers.ReadOnlyField(source='product.product_info.__str__')


	def save(self):
		product_id = self.validated_data['product']
		queryset = Product.objects.filter(id=product_id, is_available=True, is_reserved=False)
		if queryset.exists():
			queryset = queryset.first()
			queryset.update(is_reserved=True)
			return super().save()
		raise serializers.ValidationError({'error':'The product not available or reserved already.'})


class CartSerializer(serializers.ModelSerializer):
	items = serializers.SerializerMethodField()
	username=serializers.SerializerMethodField()

	def get_username(self, obj):
		return obj.user.username

	def get_items(self, obj):
		return CartItemSerializer(mymodels.CartItem.objects.filter(cart=obj), many=1).data

	class Meta:
		model = mymodels.Cart
		fields = '__all__'
