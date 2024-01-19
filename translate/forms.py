from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['choice_one', 'choice_two', 'title_type', 'page_word', 'number_page_word', 'condition']