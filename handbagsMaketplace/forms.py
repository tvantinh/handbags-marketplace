from django import forms # type: ignore
from .models import DanhMuc,SanPham

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
    Gia = forms.CharField(label='Giá', max_length=100)
    HinhAnhDaiDien = forms.CharField(label='Hình ảnh đại diện', max_length=100)
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

        danh_muc_instance = DanhMuc.objects.get(id=maDanhMuc)

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