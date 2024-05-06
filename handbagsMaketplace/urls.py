from django.urls import path
from . import views  # call to url_shortener/views.py

urlpatterns = [
    path('', views.index, name='index'),
]
