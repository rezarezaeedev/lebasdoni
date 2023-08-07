from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators

User = get_user_model()


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=300)
	postalcode = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)])
	phone=models.CharField(max_length=11, validators=[validators.MinLengthValidator(10)], help_text='Insert Like 0930***2905/مانند روبرو وارد کنید')

	def __str__(self):
		return f'{self.user.username}-{self.city}-{self.phone}'
