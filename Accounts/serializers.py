from  rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models as mymodels

User = get_user_model()


class RegisterationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=1)

	class Meta:
		model = User
		fields = '__all__'


	def save(self):
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		username = self.validated_data['username']
		email = self.validated_data['email']
		error_flag = False
		errors = {}

		if User.objects.filter(username = username).exists():
			error_flag = True
			errors.update({'username':'This username already exists!'})

		if User.objects.filter(email = email).exists():
			error_flag = True
			errors.update({'email':'This email already exists!'})

		if password != password2:
			error_flag = True
			errors.update({'password':'Two password should be same!'})

		if error_flag:
			raise serializers.ValidationError(errors)
		else:
			user = User(username=username, email=email)
			user.set_password(password)
			user.save()
			return user		


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = mymodels.Profile



