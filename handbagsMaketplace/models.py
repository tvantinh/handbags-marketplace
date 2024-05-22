from django.db import models # type: ignore

class Admin(models.Model):
    tendangnhap = models.CharField(max_length=100)
    matkhau = models.CharField(max_length=100)

    def __str__(self):
        return self.tendangnhap

class DanhMuc(models.Model):
    TenDanhMuc = models.CharField(max_length=255)

    def __str__(self):
        return self.TenDanhMuc

class SanPham(models.Model):
    MaDanhMuc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)
    TenSanPham = models.CharField(max_length=255)
    MoTa = models.TextField()
    Gia = models.DecimalField(max_digits=10, decimal_places=2)
    HinhAnhDaiDien = models.CharField(max_length=100, blank=True, null=True)
    NhanHieu = models.CharField(max_length=100, blank=True, null=True)
    ChatLieu = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.TenSanPham

class ChiTietSanPham(models.Model):
    MauSac = models.CharField(max_length=50)
    HinhAnhChiTiet = models.CharField(max_length=1000, blank=True, null=True)
    SoLuong = models.IntegerField()

    def __str__(self):
        return f"{self.MaSanPham.TenSanPham} - {self.MauSac}"

class KhachHang(models.Model):
    Ten = models.CharField(max_length=100)
    DiaChi = models.CharField(max_length=255)
    SoDienThoai = models.CharField(max_length=20)
    Email = models.EmailField(max_length=255, unique=True)
    TenDangNhap = models.CharField(max_length=100)
    MatKhau = models.CharField(max_length=100)

    def __str__(self):
        return self.Ten

class DonHang(models.Model):
    MaKhachHang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NgayDatHang = models.DateField()
    TongTien = models.DecimalField(max_digits=10, decimal_places=2)
    DiaChiGiaoHang = models.CharField(max_length=255)
    TrangThai = models.BooleanField(default=False)
    MaKhuyenMai = models.ForeignKey('KhuyenMai', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.MaDonHang

class ChiTietDonHang(models.Model):
    MaDonHang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    MaSanPham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    SoLuong = models.IntegerField()
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.MaDonHang.MaDonHang} - {self.MaSanPham.TenSanPham}"

class KhuyenMai(models.Model):
    TenKhuyenMai = models.CharField(max_length=100)
    NgayBatDau = models.DateField()
    NgayKetThuc = models.DateField()
    MoTa = models.TextField()
    GiamGia = models.IntegerField()

    def __str__(self):
        return self.TenKhuyenMai
