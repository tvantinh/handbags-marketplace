from django.urls import path # type: ignore
from . import views  # call to url_shortener/views.py

urlpatterns = [
    path('', views.List, name='loai_san_pham'),
]

