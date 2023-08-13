from django.urls import path, include
from . import views as myviews
from rest_framework.routers import DefaultRouter

app_name = 'cart-app'

router=DefaultRouter()
router.register(r'cart', myviews.CartViews)
router.register(r'cart-item', myviews.CartItemViews)


urlpatterns = [
	path('', include(router.urls))	
]

