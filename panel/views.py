from django.shortcuts import render

def test(request):
    return render(request, 'panel/base.html')

def dashboard(request):
    return render(request, 'panel/dashboard.html')

def cart(request):
    return render(request, 'panel/cart.html')

def employment(request):
    return render(request, 'panel/employment.html')

def orders_transactions(request):
    return render(request, 'panel/orders-transactions.html')

def ticket(request):
    return render(request, 'panel/ticket.html')