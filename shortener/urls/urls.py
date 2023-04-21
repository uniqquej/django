from django.urls import path
from shortener.urls import views
from rest_framework import routers
from shortener.urls.apis import *

router = routers.DefaultRouter()

# localhost:8000/api/urls/~
router.register(r'urls', UrlListView)

urlpatterns = [
    path('', views.url_list, name='url_list'),
    path('create', views.url_create, name='url_create'),
    path('<str:action>/<int:url_id>', views.url_change, name='url_change')
]
