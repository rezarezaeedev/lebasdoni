from django.urls import path, include
from .views import registeration_view
from rest_framework_simplejwt import views
from rest_framework.routers import DefaultRouter
from . import views as myviews

app_name = 'accounts'


router = DefaultRouter()
router.register('profile', myviews.ProfileView)


urlpatterns = [
    path('register/', registeration_view, name = 'register'),
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh-token/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify-token/', views.TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls))
]
