from django.urls import path, include
from .views import CartViews
from rest_framework.routers import DefaultRouter

app_name = 'cart-app'

router=DefaultRouter()
router.register('cart', CartViews)


urlpatterns = [
	
] + router.urls

