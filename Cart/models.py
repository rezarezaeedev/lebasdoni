from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	paid_at = models.DateTimeField(null=True, blank=1)
	is_paid = models.BooleanField(default=False)

	def __str__(self):
		created_at = self.created_at.strftime('%Y/%m/%d, %H:%M:%S')
		paid_at	= self.paid_at.strftime('%Y/%m/%d, %H:%M:%S') if self.paid_at else "Not paid"
		return f'{self.user.username} - created at: {created_at=} - {paid_at=}'


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey('Warehouse.Product', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.cart.user.username} - {self.product.product_info.name} - {self.cart.paid_at or "Not Paid"}'
	

