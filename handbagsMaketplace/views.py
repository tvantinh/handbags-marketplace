from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from handbagsMaketplace.forms import DanhMucForm # type: ignore
from .models import DanhMuc
#Create your views here.
def List(request):
	data = {
		'handbagsMaketplace_DanhMuc' : DanhMuc.objects.all(),
	}
	return render(request, 'admin/LoaiSanPham.html',data)

def loai_san_pham(request):
    if request.method == 'POST':
        form = DanhMucForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoaiSanPham')  # type: ignore # Thay thế bằng URL tương ứng của bạn
    else:
        form = DanhMucForm()

    danh_muc_list = DanhMuc.objects.all()
    return render(request, 'LoaiSanPham.html', {'form': form, 'handbagsMaketplace_DanhMuc': danh_muc_list})