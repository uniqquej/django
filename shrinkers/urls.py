import debug_toolbar
from django.conf.urls import include
from shortener.views import index, get_user, list_view, register, login_view, logout_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
    path("", index, name="index"),
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("list", list_view, name="list_view"),
    path("get_user/<int:user_id>", get_user),
    path('urls/', include('shortener.urls.urls')),
]
