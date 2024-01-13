from django.shortcuts import render
from .models import Product, Weblog

def index(request):
    products = Product.objects.all()
    weblogs = Weblog.objects.all()
    return render(request, 'translate/index.html', {'products': products, 'weblogs': weblogs})
