from django.db import models
from account.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    price = models.IntegerField() # price for each word
    features = models.JSONField()

    def __str__(self):
        return self.title
