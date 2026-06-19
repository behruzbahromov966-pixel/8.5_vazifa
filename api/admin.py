from django.contrib import admin

from .models import Car, CarBrand
# Register your models here.

admin.site.register([Car, CarBrand])