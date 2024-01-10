from django.shortcuts import render

def test(request):
    return render(request, 'panel/base.html')

def dashboard(request):
    return render(request, 'panel/dashboard.html')

def cart(request):
    return render(request, 'panel/cart.html')