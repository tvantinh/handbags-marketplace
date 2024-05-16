from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
#Create your views here.
def index(request):
	return render(request, 'admin/home.html')
