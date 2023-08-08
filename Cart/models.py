from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	paid_at = models.DateTimeField(null=True, blank=1)
	is_paid = models.BooleanField(default=False)


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey('Warehouse.Product', on_delete=models.CASCADE)
	

