from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=100)
    category = models.CharField(max_length=20)
    producer = models.CharField(max_length=50)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300 , null=True, default="" , blank=True )
    thumbnail = models.URLField()
    is_featured = models.BooleanField(default=False)
