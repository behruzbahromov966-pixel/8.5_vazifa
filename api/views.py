from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from .permissions import MyAuthenticatedOrReadOnly, MyAdminOnly
from .models import Car, CarBrand, Comment
from .serializer import CarSerializer ,CarBrandSerializer, CommentSerializer, CarBrandSerializerForDetail
# Create your views here.

class BrandPaginator(CursorPagination):
    page_size = 2
    ordering = ['name']

class CarBrandViewSet(ModelViewSet):
    # queryset = CarBrand.objects.all().prefetch_related('cars').only('id', 'name')
    queryset = CarBrand.objects.all().prefetch_related('cars').defer('country')
    serializer_class = CarBrandSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'country']
    ordering_fields = ['name', 'country']
    filterset_fields = ['name', 'country']
    pagination_class = BrandPaginator

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return CarBrandSerializerForDetail
        return self.serializer_class

class CarPaginator(LimitOffsetPagination):
    page_size = 2
    ordering = ['name']

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all().select_related('brand')
    serializer_class = CarSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['model_name', 'price']
    ordering_fields = ['model_name', 'price']
    filterset_fields = ['model_name', 'price', 'year']
    pagination_class = CarPaginator

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

class CommentPaginator(PageNumberPagination):
    page_size = 2
    ordering = ['name']

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['text']
    ordering_fields = ['text']
    filterset_fields = ['text']
    pagination_class = CommentPaginator

# class CarBrandApiView(ListCreateAPIView):
#     queryset = CarBrand.objects.all()
#     serializer_class = CarBrandSerializer
#     permission_classes = [MyAuthenticatedOrReadOnly]
#
# class CarBrandDetailApiView(RetrieveUpdateDestroyAPIView):
#     queryset = CarBrand.objects.all()
#     serializer_class = CarBrandSerializer
#
# class CarApiView(ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     lookup_field = 'brand_id'
#
#     def get_queryset(self):
#         brand_id = self.kwargs.get("brand_id")
#
#         min_price = self.request.query_params.get('min_price')
#         max_price = self.request.query_params.get('max_price')
#
#         if brand_id:
#             queryset = self.queryset.filter(brand_id=brand_id)
#         else:
#             queryset = self.queryset.all()
#
#         if min_price and max_price:
#             queryset = queryset.filter(price__lte=max_price, price__gte=min_price)
#         elif min_price:
#             queryset = queryset.filter(price__gte=min_price)
#         elif max_price:
#             queryset = queryset.filter(price__lte=max_price)
#         return queryset
#
# class CarDetailApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, MyAdminOnly]
#
# class CommentApiView(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [MyAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.validated_data['user'] = self.request.user
#         serializer.validated_data['car_id'] = self.kwargs.get("car_id")
#         serializer.save()
#
# class CommentDetailApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [MyAuthenticatedOrReadOnly]