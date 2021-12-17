from django.db import models

# Create your models here.
class Laptop(models.Model):
    model_name=models.CharField(max_length=50)
    ram=models.IntegerField()
    rom=models.FloatField()
    processor=models.FloatField()
    price=models.FloatField()
    weight=models.FloatField()
