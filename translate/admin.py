from django.contrib import admin
from .models import Product, Weblog, Choice, TitleType, Order

admin.site.register(Product)
admin.site.register(Weblog)
admin.site.register(Choice)
admin.site.register(TitleType)
admin.site.register(Order)