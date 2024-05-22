from django import forms # type: ignore
from .models import DanhMuc

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

