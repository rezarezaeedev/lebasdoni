from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warehouse/', include('Warehouse.urls')),
    path('account/', include('Accounts.urls')),
    path('payment/', include('Payment.urls')),
]
