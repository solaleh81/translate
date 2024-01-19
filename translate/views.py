from django.shortcuts import render, redirect
from .models import Product, Weblog, ChoiceOne, ChoiceTwo, TitleType, ConditionType
from .forms import OrderForm


def index(request):
    products = Product.objects.all()
    weblogs = Weblog.objects.all()
    return render(request, 'translate/index.html', {'products': products, 'weblogs': weblogs})


def service1(request):
    products = Product.objects.all()
    choices1 = ChoiceOne.objects.all()
    choices2 = ChoiceTwo.objects.all()
    titles = TitleType.objects.all()
    conditions = ConditionType.objects.all()
    return render(request, 'translate/service_1.html', {
        'products': products, 'choices1': choices1, 'choices2': choices2, 'titles': titles, 'conditions': conditions}
                  )


def success(request):
    return render(request, 'translate/success_page.html')


def create_order(request):
    print("Request method:", request.method)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            print("Order saved successfully:", order)
            return redirect('success')
        else:
            print("Form is invalid:", form.errors)
    products = Product.objects.all()
    choices1 = ChoiceOne.objects.all()
    choices2 = ChoiceTwo.objects.all()
    titles = TitleType.objects.all()
    conditions = ConditionType.objects.all()
    form = OrderForm()
    return render(request, 'translate/service_1.html',
                  {'form': form, 'products': products, 'choices1': choices1, 'choices2': choices2, 'titles': titles,
                   'conditions': conditions})
