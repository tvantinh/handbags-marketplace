from django.urls import path # type: ignore
from . import views  # call to url_shortener/views.py

urlpatterns = [
    path('', views.List, name='index'),
    path('dsLoaiSanPham', views.loai_san_pham, name='dsLoaiSanPham'),
    path('dssanpham',views.san_pham,name='dssanpham'),
]

