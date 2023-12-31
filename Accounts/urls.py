from django.urls import path, include
from .views import registeration_view
from rest_framework_simplejwt import views
from . import views as myviews

app_name = 'accounts'


urlpatterns = [
    path('register/', registeration_view, name = 'register'),
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh-token/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify-token/', views.TokenVerifyView.as_view(), name='token_verify'),
    path('profile/<user__username>/', myviews.ProfileView.as_view()),
    path('<username>/verify/<verification_token>/', myviews.activate_view),
]
