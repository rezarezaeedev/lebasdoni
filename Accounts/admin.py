from django.contrib import admin
from . import models as mymodels


@admin.register(mymodels.Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass


@admin.register(mymodels.NewUser)
class NewUserAdmin(admin.ModelAdmin):
	pass
