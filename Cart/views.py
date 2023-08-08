from . import models as mymodels 
from . import serializers as myserializers 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class CartViews(ModelViewSet):
	serializer_class = myserializers.CartSerializer
	lookup_field = 'username'
	queryset = mymodels.Cart.objects.all()


	def retrieve(self, request, username, *args, **kwargs):
		if request.user.username == username:
			queryset = mymodels.Cart.objects.get(is_paid=0, user__username=request.user.username)
			serializer = myserializers.CartSerializer(queryset)
			return Response(serializer.data, status=200)
		return Response({'error':'You can view your account carts.'}, status=404)


