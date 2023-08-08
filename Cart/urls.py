from django.urls import path, include
from . import views as myviews
from rest_framework.routers import DefaultRouter

app_name = 'cart-app'

router=DefaultRouter()
router.register('cart', myviews.CartViews)
router.register('cart-item', myviews.CartItemViews)


urlpatterns = [
	path('', include(router.urls))	
]

