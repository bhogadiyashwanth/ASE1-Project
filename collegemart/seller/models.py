from django.db import models
from registration.models import Profile

#Create your models here.

CATEGORY_CHOICES = (
        ('Hostel', 'Hostel'),
        ('Lab', 'Lab'),
        ('Books', 'Books'),
    )

class Category(models.Model):

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    def __str__(self):
        return self.category

class Products_Selling(models.Model):
    pname = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to = 'SellingProductsPhotos/', default = 'SellingProductsPhotos/None/no-img.jpg')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Seller = models.ManyToManyField(Profile)
    amount = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.pname

    def __repr__(self):
        return self.pname
