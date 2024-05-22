from django.shortcuts import render # type: ignore
from django.http import HttpResponse, HttpResponseRedirect# type: ignore
from handbagsMaketplace.forms import DanhMucForm # type: ignore
from .models import DanhMuc
#Create your views here.
def List(request):
	data = {
		'handbagsMaketplace_DanhMuc' : DanhMuc.objects.all(),
	}
	return render(request, 'admin/SanPham.html',data)

def loai_san_pham(request):
    form = DanhMucForm()
    if request.method == 'POST':
        form = DanhMucForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/handbagsMaketplace/dsLoaiSanPham')  # type: ignore # Thay thế bằng URL tương ứng của bạn
    else:
       data = {
            'form':form,
            'handbagsMaketplace_DanhMuc' : DanhMuc.objects.all(),
       }
    return render(request, 'admin/LoaiSanPham.html', data)