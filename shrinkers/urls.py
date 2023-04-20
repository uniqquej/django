import debug_toolbar
from django.conf.urls import include
from shortener.urls.views import url_redirect
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    path('urls/', include('shortener.urls.urls')),
    path('<str:prefix>/<str:url>',url_redirect )
]
