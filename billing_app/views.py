from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def shop_details(request):
    return render(request, 'masters/shop_details.html')

def sub_admin(request):
    return render(request, 'masters/sub_admin.html')

def shop_keeper(request):
    return render(request, 'masters/shop_keeper.html')

def products(request):
    return render(request, 'masters/products.html')

def brands(request):
    return render(request, 'masters/brands.html')

def sales_report(request):
    return render(request, 'reports/sales_report.html')

def products_report(request):
    return render(request, 'reports/products_report.html')