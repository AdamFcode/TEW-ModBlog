from . import views
from django.urls import path

urlpatterns = [
    path('', views.link, name='link'),
]