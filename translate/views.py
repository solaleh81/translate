from django.shortcuts import render
from .models import Product, Weblog, Choice


def index(request):
    products = Product.objects.all()
    weblogs = Weblog.objects.all()
    return render(request, 'translate/index.html', {'products': products, 'weblogs': weblogs})

def service1(request):
    products = Product.objects.all()
    choices = Choice.objects.all()
    return render(request, 'translate/service_1.html', {'products': products, 'choices': choices})
