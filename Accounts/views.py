from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import RegisterationSerializer, ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from . import models as mymodels


@api_view(['POST',])
def registeration_view(request):
	data = {}
	serializer = RegisterationSerializer(data = request.data)
	if serializer.is_valid():
		user = serializer.save()
		refresh = RefreshToken.for_user(user)
		data.update({'username':user.username, 'token':{'refresh':str(refresh), 'access':str(refresh.access_token),}})
	else:
		data = serializer.errors

	return Response(data, status=status.HTTP_201_CREATED)


class ProfileView(ModelViewSet):
	queryset = mymodels.Profile.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'user__username'

	def list(self, request):
		return Response({'error':'Not found!'}, status=404)


