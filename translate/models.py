from django.db import models
from account.models import User
from persiantools import jdatetime
from datetime import datetime  # Import the datetime module




class Product(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    price = models.IntegerField()  # price for each word
    features = models.JSONField()

    def __str__(self):
        return self.title


class Choice(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class TitleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ConditionType(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):

    class PageWord(models.TextChoices):
        PAGE = (
            "1",
            "page",
        )
        WORD = (
            "2",
            "word",
        )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    choice_one = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='orders')
    title_type = models.ForeignKey(TitleType, on_delete=models.PROTECT, related_name='orders')
    page_word = models.CharField(max_length=1, choices=PageWord.choices)
    number_page_word = models.IntegerField()
    condition = models.ForeignKey(ConditionType, on_delete=models.PROTECT, related_name='orders')

    @property
    def price(self):
        price = self.page_word * self.number_page_word
        return price

class Weblog(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    caption = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def jalali_created_date(self):
        # Convert created_date to a standard Python datetime object
        standard_datetime = datetime.combine(self.created_date.date(), self.created_date.time())

        # Convert the standard datetime object to JalaliDateTime
        jalali_datetime = jdatetime.JalaliDateTime.to_jalali(standard_datetime)
        mapping = {
            1: "فروردین",
            2: "اردیبهشت",
            3: "خرداد",
            4: "تیر",
            5: "مرداد",
            6: "شهریور",
            7: "مهر",
            8: "آبان",
            9: "آذر",
            10: "دی",
            11: "بهمن",
            12: "اسفند",
        }
        persian_month_name = mapping[jalali_datetime.month]
        persian_year = jalali_datetime.strftime("%Y")

        return f"{persian_month_name} {persian_year}"

    def __str__(self):
        return self.title

