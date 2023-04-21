import debug_toolbar
from django.conf.urls import include
from shortener.urls.urls import router as url_router
from shortener.urls.views import url_redirect
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    path('index/', include('shortener.index.urls')),
    path('urls/', include('shortener.urls.urls')),
    path('api/', include(url_router.urls)),
    path('<str:prefix>/<str:url>', url_redirect )
]
