from . import models as mymodels 
from . import serializers as myserializers 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


class CartViews(ModelViewSet):
	serializer_class = myserializers.CartSerializer
	queryset 		 = mymodels.Cart.objects.all()


	def get_queryset(self):
		queryset = mymodels.Cart.objects.filter(is_paid=0, user__username=self.request.user.username)
		return queryset


	def update(self, request, pk):
		return Response({'errors':'METHOD NOT ALLOWED'}, status=HTTP_405_METHOD_NOT_ALLOWED)
		
	def partial_update(self, request, pk):
		return Response({'errors':'METHOD NOT ALLOWED'}, status=HTTP_405_METHOD_NOT_ALLOWED)



class CartItemViews(ModelViewSet):
	serializer_class = myserializers.CartItemSerializer
	queryset 		 = mymodels.CartItem.objects.all()


	def get_queryset(self):
		queryset 	 = mymodels.CartItem.objects.filter(cart__user__id=self.request.user.id)
		return queryset

	def update(self, request, pk):
		return Response({'errors':'METHOD NOT ALLOWED'}, status=HTTP_405_METHOD_NOT_ALLOWED)

	def partial_update(self, request, pk):
		return Response({'errors':'METHOD NOT ALLOWED'}, status=HTTP_405_METHOD_NOT_ALLOWED)
	


