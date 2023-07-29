from django.db import models


class ProductInfo(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=20)
	price = models.FloatField()
	# sex = FK to sex model
	# material = FK 2 Material 
	# size = FK to size model

