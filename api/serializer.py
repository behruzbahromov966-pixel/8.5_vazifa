from rest_framework import serializers

from .models import CarBrand, Car

class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        depth = 1