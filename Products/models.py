from django.db import models


class Sex(models.Model):
	sex = models.BooleanField(help_text="True meant Man's sex and False is Woman")

	def __str__(self):
		return 'Man' if self.sex else 'Woman'


class ProductInfo(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	price = models.FloatField()
	sex = models.ForeignKey('Sex', on_delete=models.CASCADE)
	size = models.SmallIntegerField()
	# material = FK 2 Material 

	def __str__(self):
		return f'{self.name} {self.color} {self.price}'


class Product(models.Model):
	product_info = models.ForeignKey('ProductInfo', on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	is_reserved  = models.BooleanField(default=False)
	imported_time = models.DateTimeField(auto_now_add=True, editable=False)
	exported_time = models.DateTimeField(null=True, blank=True, editable=False)

	def __str__(self):
		return f'Availablity:{self.is_available} ,Reservilty:{self.is_reserved}'