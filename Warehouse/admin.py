from django.contrib import admin
from . import models


@admin.register(models.ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
	list_display=['__str__','active']
	list_editable = ['active']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Sex)
class SexAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(models.ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
	list_display=['__str__','active']
	list_editable = ['active']


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
	pass
