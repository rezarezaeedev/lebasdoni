from . import models as mymodels 
from . import serializers as myserializers 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class CartViews(ModelViewSet):
	serializer_class = myserializers.CartSerializer
	queryset =mymodels.Cart.objects.all()


	def get_queryset(self):
		queryset = mymodels.Cart.objects.filter(is_paid=0, user__username=self.request.user.username)
		return queryset


