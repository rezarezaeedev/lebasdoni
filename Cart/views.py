from . import models as mymodels 
from . import serializers as myserializers 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from Permissions.permissions import IsOwnerUser
from drf_yasg.utils import swagger_auto_schema


class CartViews(ModelViewSet):
	permission_classes = [IsOwnerUser]
	serializer_class = myserializers.CartSerializer
	queryset 		 = mymodels.Cart.objects.all()


	def get_queryset(self):
		queryset = mymodels.Cart.objects.filter(user__username=self.request.user.username)
		return queryset

	def update(self, request, pk):
		'Uses for set paid status after success payment.'
		data_to_change = {'is_paid':True, 'paid_at':datetime.today()}
		queryset = self.get_object()
		serializer = self.get_serializer(queryset ,data=data_to_change, partial=True)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response({'message':'Yor cart paid successfuly', **serializer.data}, status=200)

		
	def partial_update(self, request, pk):
		return self.update(request, pk)


class CartItemViews(ModelViewSet):
	permission_classes = [IsOwnerUser]
	serializer_class = myserializers.CartItemSerializer
	queryset 		 = mymodels.CartItem.objects.all()


	def get_queryset(self):
		queryset 	 = mymodels.CartItem.objects.filter(cart__user__id=self.request.user.id)
		return queryset

	def update(self, request, pk):
		return Response({'errors':'METHOD NOT ALLOWED'}, status=HTTP_405_METHOD_NOT_ALLOWED)

	def partial_update(self, request, pk):
		return Response({'errors':'METHOD NOT ALLOWED'}, status=HTTP_405_METHOD_NOT_ALLOWED)
	


