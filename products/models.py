from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    
    
