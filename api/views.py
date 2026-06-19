from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import Car, CarBrand
from .serializer import CarSerializer ,CarBrandSerializer
# Create your views here.

class CarBrandApiView(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarBrandDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarApiView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'brand_id'

    def get_queryset(self):
        brand_id = self.kwargs.get("brand_id")

        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if brand_id:
            queryset = self.queryset.filter(brand_id=brand_id)
        else:
            queryset = self.queryset.all()

        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price, price__gte=min_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

class CarDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer