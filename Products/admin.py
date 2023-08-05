from django.contrib import admin
from . import models

@admin.register(models.ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Product)
class ProductInfoAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Sex)
class SexInfoAdmin(admin.ModelAdmin):
	pass

