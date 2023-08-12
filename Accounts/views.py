from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from .serializers import RegisterationSerializer, ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from . import models as mymodels
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


User = get_user_model()
group, created = Group.objects.get_or_create(name='CustomerUser')


def send_verification_email(user):
	verification_token = default_token_generator.make_token(user)
	username = user.username
	verification_link = f'http:localhost:8000/account/{username}/verify/{verification_token}/'
	subject = 'Verify Your Account'
	message = f'Click the link to verify your account: {verification_link}'
	from_email = 'noreply@yourdomain.com'
	recipient_list = [user.email]
	
	send_mail(subject, message, from_email, recipient_list)


@api_view(['POST',])
def registeration_view(request):
	data={}
	serializer = RegisterationSerializer(data = request.data)
	if serializer.is_valid():
		data.update({'message':'Please checkyour email and verify your account.'})
		user = serializer.save()
		user.groups.add(group)
		send_verification_email(user)
	else:
		data = serializer.errors

	return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET',])
def activate_view(request, username=None, verification_token=None):
	data = {}
	if username:
		user = User.objects.filter(username=username)
		if user.exists():
			user= user.first()
			if default_token_generator.check_token(user, verification_token):
				user.is_verified = True
				user.save()
				refresh = RefreshToken.for_user(user)
				data.update({'username':user.username, 'token':{'refresh':str(refresh), 'access':str(refresh.access_token)}})
				return Response(data, status=status.HTTP_200_OK)
		return Response({'error':'Not found user or Invalid token.'}, status=status.HTTP_200_OK)

	if user is None:
		return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
	if not default_token_generator.check_token(user, confirmation_token):
		return Response('Token is invalid or expired. Please request another confirmation email by signing in.', status=status.HTTP_400_BAD_REQUEST)
	user.is_active = True
	user.save()
	return Response('Email successfully confirmed')


class ProfileView(RetrieveUpdateAPIView):
	queryset = mymodels.Profile.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'user__username'
