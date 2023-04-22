# import debug_toolbar
from django.conf.urls import include
from shortener.urls.urls import router as url_router
from shortener.urls.views import url_redirect
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#django-ninga
from ninja import NinjaAPI
from shortener.users.apis import user as user_router

schema_view = get_schema_view(
   openapi.Info(
      title="Shrinkers API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

apis = NinjaAPI(title='Shrinkers API')
apis.add_router("/users/", user_router, tags = ['Common'])

urlpatterns = [
    # path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path('index/', include('shortener.index.urls')),
    path('urls/', include('shortener.urls.urls')),
    path('api/', include(url_router.urls)),
    path('ninja-api/', apis.urls),
    path('<str:prefix>/<str:url>', url_redirect )
]