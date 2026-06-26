from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.model_name

class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text