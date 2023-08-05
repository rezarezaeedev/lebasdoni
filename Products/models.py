from django.db import models


class ProductInfo(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	price = models.FloatField()
	# sex = FK to sex model
	# material = FK 2 Material 
	# size = FK to size model

	def str(self):
		return f'{self.name} {self.color} {self.price}'


class Product(models.Model):
	product_info = models.ForeignKey('ProductInfo', on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	is_reserved  = models.BooleanField(default=False)
	imported_time = models.DateTimeField(auto_now_add=True, editable=False)
	exported_time = models.DateTimeField(null=True, blank=True, editable=False)

	def str(self):
		return f'Availablity:{self.is_available} ,Reservilty:{self.is_reserved}'