import os
from django import forms # type: ignore

from nhom7 import settings # type: ignore
from .models import DanhMuc,SanPham,KhachHang
from django.core.files.storage import FileSystemStorage # type: ignore

class DangNhapForm(forms.Form):
    TenDangNhap = forms.CharField(max_length=100)
    MatKhau = forms.CharField(widget=forms.PasswordInput)


class DangKyForm(forms.ModelForm):
    MatKhau = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = KhachHang
        fields = ['Ten', 'DiaChi', 'SoDienThoai', 'Email', 'TenDangNhap', 'MatKhau']


class DanhMucForm(forms.Form):
    TenDanhMuc = forms.CharField(label='Tên Danh Mục',max_length=100)
    def clean_TenDanhMuc(self):
        TenDanhMuc = self.cleaned_data['TenDanhMuc']
        try:
            DanhMuc.objects.get(TenDanhMuc = TenDanhMuc)
        except DanhMuc.DoesNotExist:
            return TenDanhMuc
        raise forms.ValidationError("Danh mục đã tồn tại! ")
    def save(self):
        DanhMuc.objects.create(TenDanhMuc = self.cleaned_data['TenDanhMuc'])



class SanPhamForm(forms.Form):
    MaDanhMuc = forms.ChoiceField(
        label='Mã danh mục',
        choices=[],  # Khởi tạo với danh sách rỗng, sẽ được cập nhật trong __init__
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    TenSanPham = forms.CharField(label='Tên Sản Phẩm', max_length=100)
    MoTa = forms.CharField(label='Mô tả', max_length=100)
    Gia = forms.DecimalField(label='Giá', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    HinhAnhDaiDien = forms.ImageField(label='Hình ảnh đại diện', max_length=100)
    NhanHieu = forms.CharField(label='Nhãn hiệu', max_length=100)
    ChatLieu = forms.CharField(label='Chất liệu', max_length=100)

    def clean_TenSanPham(self):
        TenSanPham = self.cleaned_data['TenSanPham']
        try:
            SanPham.objects.get(TenSanPham=TenSanPham)
        except SanPham.DoesNotExist:
            return TenSanPham
        raise forms.ValidationError("Sản phẩm đã tồn tại! vui lòng đặt tên mới!!!")

    def save(self):
        maDanhMuc = self.cleaned_data['MaDanhMuc']
        tenSanPham = self.cleaned_data['TenSanPham']
        moTa = self.cleaned_data['MoTa']
        gia = self.cleaned_data['Gia']
        hinhAnhDaiDien = self.cleaned_data['HinhAnhDaiDien']
        nhanHieu = self.cleaned_data['NhanHieu']
        chatLieu = self.cleaned_data['ChatLieu']

        danh_muc_instance = DanhMuc.objects.get(MaDanhMuc=maDanhMuc)

        fs = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'static/img'))
        filename = fs.save(hinhAnhDaiDien.name, hinhAnhDaiDien)
        hinhAnhDaiDien_url = os.path.join('img', filename)
        # Tạo đối tượng SanPham và lưu vào cơ sở dữ liệu
        sanpham = SanPham.objects.create(
            TenSanPham=tenSanPham,
            MoTa=moTa,
            Gia=gia,
            HinhAnhDaiDien=hinhAnhDaiDien,
            NhanHieu=nhanHieu,
            ChatLieu=chatLieu,
            MaDanhMuc=danh_muc_instance
        )
        return sanpham

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['MaDanhMuc'].choices = [
            (dm.pk, dm.TenDanhMuc) for dm in DanhMuc.objects.all()
        ]


class DanhMucForm(forms.ModelForm):
    class Meta:
        model = DanhMuc
        fields = ['TenDanhMuc']
        widgets = {
            'TenDanhMuc': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['MaDanhMuc', 'TenSanPham', 'MoTa', 'Gia', 'HinhAnhDaiDien', 'NhanHieu', 'ChatLieu']
        widgets = {
            'MaDanhMuc': forms.Select(attrs={'class': 'form-control'}),
            'TenSanPham': forms.TextInput(attrs={'class': 'form-control'}),
            'MoTa': forms.TextInput(attrs={'class': 'form-control'}),
            'Gia': forms.TextInput(attrs={'class': 'form-control'}),
            'HinhAnhDaiDien': forms.FileInput(attrs={'class': 'form-control'}),
            'NhanHieu': forms.TextInput(attrs={'class': 'form-control'}),
            'ChatLieu': forms.TextInput(attrs={'class': 'form-control'}),
        }