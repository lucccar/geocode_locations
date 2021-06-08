from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from app.views import CustomerView


schema_view = get_schema_view(
    openapi.Info(
        title="Geocoding API",
        default_version='v1',
        description="A geocode retriever",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="lucas.crvlh.s@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    path('customers/<int:id>/', CustomerView.as_view(), name='customer-by-id'),
    path('customers/', CustomerView.as_view(), name='all-customers'),
]
