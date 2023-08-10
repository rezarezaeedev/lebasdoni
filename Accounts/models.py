from django.db import models
from django.core import validators
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=30)
	address = models.CharField(max_length=300)
	postalcode = models.CharField(max_length=10, validators=[validators.MinLengthValidator(10)])
	phone=models.CharField(max_length=11, validators=[validators.MinLengthValidator(10)], help_text='Insert Like 0930***2905/مانند روبرو وارد کنید')
	image = models.ImageField(upload_to='Media/user uploded/', null=1, blank=1)

	def __str__(self):
		return f'{self.user.username}-{self.city}-{self.phone}'
