from django.db import models
from account.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    price = models.IntegerField() # price for each word
    features = models.JSONField()

    def __str__(self):
        return self.title
