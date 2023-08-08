from django.contrib import admin
from . import models as mymodels


@admin.register(mymodels.Cart)
class CartAdmin(admin.ModelAdmin):
	pass


@admin.register(mymodels.CartItem)
class CartItemAdmin(admin.ModelAdmin):
	pass
