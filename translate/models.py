from django.db import models
from account.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    price = models.IntegerField()  # price for each word
    features = models.JSONField()

    def __str__(self):
        return self.title


class Choice(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TitleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    class ConditionType(models.TextChoices):
        FORCE = (
            "1",
            "force",
        )
        NORMAL = (
            "2",
            "normal",
        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    choice_one = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='orders')
    title_type = models.ForeignKey(TitleType, on_delete=models.PROTECT, related_name='orders')
    page_word = models.CharField(max_length=1, choices=PageWord.choices)
    number_page_word = models.IntegerField()
    condition = models.CharField(max_length=1, choices=ConditionType.choices)

    @property
    def price(self):
        price = self.page_word * self.number_page_word
        return price

class Weblog(models.Model):
    image = models.ImageField(upload_to="weblog/%Y/%m/", null=True, blank=True)
    title = models.CharField(max_length=100)
    caption = models.TextField()

    def __str__(self):
        return self.title

