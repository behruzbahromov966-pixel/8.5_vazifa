from rest_framework import serializers

from .models import CarBrand, Car, Comment

class CarSerializerForBrand(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['brand']

class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBrand
        exclude = ['country']


class CarBrandSerializerForDetail(serializers.ModelSerializer):

    # cars = serializers.StringRelatedField(many=True)
    cars = CarSerializerForBrand(many=True, read_only=True)
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    url = serializers.HyperlinkedIdentityField(view_name="car-detail")
    my_brand = serializers.ChoiceField(source=CarBrand.objects.all())
    class Meta:
        model = Car
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        brand = validated_data.get("my_brand")
        car = Car.objects.create(**validated_data, brand=brand)
        return car

    def update(self, instance, validated_data):
        instance.brand = validated_data.pop('my_brand') if validated_data.get("my_brand") else instance.brand
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']