from django.shortcuts import render # type: ignore
from django.http import HttpResponse, HttpResponseRedirect# type: ignore
from handbagsMaketplace.forms import DanhMucForm, SanPhamForm,DangKyForm, DangNhapForm# type: ignore
from .models import DanhMuc,SanPham,ChiTietSanPham,DonHang,KhachHang
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
#Create your views here.
def List(request):
	data = {
		'handbagsMaketplace_DanhMuc' : DanhMuc.objects.all(),
	}
	return render(request, 'admin/SanPham.html',data)

def dskhachhang(request):
    khach_hang_list = KhachHang.objects.all()
    return render(request, 'admin/DanhSachKhachHang.html', {'khach_hang_list': khach_hang_list})
def dstkkh(request):
    khach_hang_list = KhachHang.objects.all()
    return render(request, 'admin/DanhSachTaiKhoanKH.html', {'khach_hang_list': khach_hang_list})

def lichSuDonHang(request):
    data = {
		'handbagsMaketplace_donhang' : DonHang.objects.filter(TrangThai=True),

	}
    return render(request, 'admin/LichSuDonHang.html',data)

def dsDonHang(request):
    data = {
		'handbagsMaketplace_donhang' : DonHang.objects.filter(TrangThai=False),

	}
    return render(request, 'admin/LichSuDonHang.html',data)

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

def HoanThanhDonHang(request, MaDonHang):
    don_hang = get_object_or_404(DonHang, pk=MaDonHang)
    if request.method == 'POST':
        don_hang.TrangThai = True
        don_hang.save()
        return redirect('dsdonhang')
    return redirect('dsdonhang')


def san_pham(request):
    form=SanPhamForm()
    if request.method=='POST':
        form=SanPhamForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/handbagsMaketplace/dssanpham')
    data={
        'form':form,
        'handbagsMaketplace_SanPham':SanPham.objects.all(),
    }
    return render(request,'admin/SanPham.html',data)

def xoa_danh_muc(request, MaDanhMuc):
    danh_muc = get_object_or_404(DanhMuc, pk=MaDanhMuc)
    if request.method == 'POST':
        danh_muc.delete()
        return redirect('/handbagsMaketplace/dsLoaiSanPham')

def xoaSanPham(request, MaSanPham):
    SanPhamXoa = get_object_or_404(SanPham, pk=MaSanPham)
    if request.method == 'POST':
        SanPhamXoa.delete()
        return redirect('/handbagsMaketplace/dssanpham')

def suaDanhMuc(request, MaDanhMuc):
    danh_muc = get_object_or_404(DanhMuc, pk=MaDanhMuc)
    if request.method == 'POST':
        form = DanhMucForm(request.POST, instance=danh_muc)
        if form.is_valid():
            form.save()
            return redirect('/handbagsMaketplace/dssanpham')
    else:
        form = DanhMucForm(instance=danh_muc)
    return render(request, 'admin/suaSanPham.html', {'form': form, 'san_pham': san_pham})

def suaSanPham(request, MaSanPham):
    san_pham = get_object_or_404(SanPham, pk=MaSanPham)
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES, instance=san_pham)
        if form.is_valid():
            form.save()
            return redirect('/handbagsMaketplace/dssanpham')
    else:
        form = SanPhamForm(instance=san_pham)
    return render(request, 'admin/suaSanPham.html', {'form': form, 'san_pham': san_pham})

def sanpham_theo_loai(request, loai_id):
    Madanh_muc = get_object_or_404(DanhMuc, pk=loai_id)
    san_pham_list = SanPham.objects.filter(MaDanhMuc=Madanh_muc)
    context = {
        'danh_muc': Madanh_muc,
        'san_pham_list': san_pham_list,
    }
    return render(request, 'admin/DsSanPhamTheoLoai.html', context)


def timkiem_sanpham(request):
    form=SanPhamForm()
    query=request.GET.get('q',None)
    ket_qua=SanPham.objects.none()
    
    if query:
        ket_qua=SanPham.objects.filter(TenSanPham__icontains=query)
    else:
        ket_qua=SanPham.objects.all()
       
    data={
        'ket_qua':ket_qua,
        'query':query,
        'form':form,
        'handbagsMaketplace_SanPham':SanPham.objects.all(),
        }
    return render(request,'admin/SanPham.html',data)


def timkiem_danhmuc(request):
    form=DanhMucForm()
    query=request.GET.get('q',None)
    ket_qua=DanhMuc.objects.none()
    
    if query:
        ket_qua=DanhMuc.objects.filter(TenDanhMuc__icontains=query)
    else:
        ket_qua=DanhMuc.objects.all()
       
    data={
        'ket_qua':ket_qua,
        'query':query,
        'form':form,
        'handbagsMaketplace_DanhMuc':DanhMuc.objects.all(),
        }
    return render(request,'admin/LoaiSanPham.html',data)


def DangKy(request):
    if request.method == 'POST':
        form = DangKyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/handbagsMaketplace/dangnhap')
    else:
        form = DangKyForm()
    return render(request, 'home/DangKyAccount.html', {'form': form})

def dang_nhap(request):
    if request.method == 'POST':
        form = DangNhapForm(request.POST)
        if form.is_valid():
            ten_dang_nhap = form.cleaned_data['TenDangNhap']
            mat_khau = form.cleaned_data['MatKhau']
            khach_hang = KhachHang.objects.filter(TenDangNhap=ten_dang_nhap).first()
            
            if khach_hang is not None and khach_hang.MatKhau == mat_khau:
                return redirect('/handbagsMaketplace/')  
            else:
                form.add_error(None, "Tên đăng nhập hoặc mật khẩu không chính xác.")
    else:
        form = DangNhapForm()
    return render(request, 'home/DangNhap.html', {'form': form})

def index(request, madanhmuc = None):
    categories = DanhMuc.objects.all()
    search_query = request.GET.get('searchtx')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.get('category')

    products = SanPham.objects.all()

    if request.method == 'POST':
        search_query = request.POST.get('searchtxt', '')
        products = SanPham.objects.filter(TenSanPham__icontains=search_query)
    if search_query:
        products = products.filter(TenSanPham__icontains=search_query)
    if min_price:
        products = products.filter(Gia__gte=min_price)
    if max_price:
        products = products.filter(Gia__lte=max_price)
    if category:
        products = products.filter(MaDanhMuc=category)
    elif madanhmuc:
        products = SanPham.objects.filter(MaDanhMuc=madanhmuc)

    return render(request, 'home/index.html', {'categories': categories, 'products': products})
def product_list(request):
    products = SanPham.objects.all()
    return render(request, 'home/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(SanPham, pk=pk)
    return render(request, 'home/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(SanPham, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})
    if str(product_id) in cart:  # Đảm bảo dùng khóa là chuỗi để nhất quán với view_cart
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {
            'product_id': product_id,
            'name': product.TenSanPham,
            'price': product.Gia,
            'quantity': quantity
        }

    request.session['cart'] = cart
    messages.success(request, f"Thêm {product.TenSanPham} vào giỏ hàng thành công!")
    return redirect('product_detail', pk=product_id)


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for item_id, item_data in cart.items():
        product = get_object_or_404(SanPham, pk=item_id)  # Lấy thông tin sản phẩm từ database
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'item_price': item_data['price'] * item_data['quantity']
        })

    total_quantity = sum(item['quantity'] for item in cart_items)
    total_price = sum(item['item_price'] for item in cart_items)

    return render(request, 'home/cart.html', {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_price': total_price
    })


def update_cart(request):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1))

        product = get_object_or_404(SanPham, pk=product_id)

        cart = request.session.get('cart', {})
        cart[product_id] = {
            'product_id': product_id,
            'name': product.TenSanPham,
            'price': product.Gia,
            'quantity': quantity
        }
        request.session['cart'] = cart
        messages.success(request, f"Giỏ hàng đã được cập nhật!")
        return redirect('view_cart')


def remove_from_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart
            messages.success(request, "Xóa sản phẩm khỏi giỏ hàng thành công!")

    return redirect('view_cart')

def clear_cart(request):
    if request.method == 'POST' or request.method == 'GET':
        request.session['cart'] = {}

    return redirect('view_cart')