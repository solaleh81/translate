from django.db import models
from account.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    caption = models.TextField()
    price = models.IntegerField()
    # features