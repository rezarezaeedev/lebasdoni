from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="LebasDoni API documentation",
        default_version='v1',
        description="This application is a simple assignment for mizan-gostar-elm-va-danesh company",
        terms_of_service="https://www.rezarezaeedev.github.io",
        contact=openapi.Contact(email="rezarezaee.commercial@gmail.com" ),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('warehouse/', include('Warehouse.urls')),
    path('account/', include('Accounts.urls')),
    path('account/', include('Cart.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
