from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warehouse/', include('Warehouse.urls')),
    path('accounts/', include('Accounts.urls')),
    path('drf/', include('rest_framework.urls')),
]
