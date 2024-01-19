from django.contrib import admin
from .models import Product, Weblog, ChoiceOne, ChoiceTwo, TitleType, Order, ConditionType

admin.site.register(Product)
admin.site.register(Weblog)
admin.site.register(ChoiceOne)
admin.site.register(ChoiceTwo)
admin.site.register(TitleType)
admin.site.register(Order)
admin.site.register(ConditionType)