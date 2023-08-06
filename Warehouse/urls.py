from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('product-info' ,views.ProductInfoView)
router.register('product' ,views.ProductView)
router.register('category' ,views.CategoryView)
router.register('sex' ,views.SexView)


urlpatterns = [
    path('', include(router.urls)),
    path('product-like/' ,views.LikeView.as_view(), name='product-likes'),
    path('product-comment/' ,views.ProductCommentView.as_view(), name='product-comment'),
]
