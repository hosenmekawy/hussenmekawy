from django.db import models


class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    
    
class offer(models.Model):
    code = models.CharField(max_length=10)
    discription = models.CharField(max_length=255)
    discount = models.FloatField()
    
    
