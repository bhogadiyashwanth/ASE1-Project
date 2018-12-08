from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# Create your models here.
class ProductDetails( models.Model ):
    prodID = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=150)
    prod_description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    prod_type = models.CharField(max_length=100)
    sellerID = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
