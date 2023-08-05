from django.contrib import admin
from . import models

@admin.register(models.ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Sex)
class SexAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	pass
