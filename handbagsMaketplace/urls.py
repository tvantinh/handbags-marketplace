from django.urls import path # type: ignore

from nhom7 import settings # type: ignore
from . import views  # call to url_shortener/views.py
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path('dsLoaiSanPham', views.loai_san_pham, name='dsLoaiSanPham'),
    path('dssanpham',views.san_pham,name='dssanpham'),
    path('timkiemsanpham',views.timkiem_sanpham,name='timkiemsanpham'),
    path('timkiemdanhmuc',views.timkiem_danhmuc,name='timkiemdanhmuc'),
    path('xoa_danh_muc/<int:MaDanhMuc>/', views.xoa_danh_muc, name='xoa_danh_muc'),
    path('sanpham_theo_loai/<int:loai_id>/', views.sanpham_theo_loai, name='sanpham_theo_loai'),
    path('xoaSanPham/<int:MaSanPham>/', views.xoaSanPham, name='xoaSanPham'),
    path('suaDanhMuc/<int:MaDanhMuc>/', views.suaDanhMuc, name='sua_danh_muc'),
    path('suaSanPham/<int:MaSanPham>/', views.suaSanPham, name='suaSanPham'),
    path('lichSuDonHang', views.lichSuDonHang, name='lichSuDonHang'),
    path('dsdonhang/', views.dsDonHang, name='dsdonhang'),
    path('hoanthanhdonhang/<int:MaDonHang>/', views.HoanThanhDonHang, name='hoanthanhdonhang'),
    path('dskhachhang/', views.dskhachhang, name='dskhachhang'),
    path('dangky', views.DangKy, name='dang_ky'),
    path('taikhoankh/', views.dstkkh, name='taikhoankh'),
    path('dangnhap',views.dang_nhap,name='dangnhap'),

    path('', views.index, name='index'),
    path('category/<int:madanhmuc>/', views.index, name='product_by_category'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
] 

