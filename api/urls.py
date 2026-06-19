from django.urls import path

from .views import CarApiView, CarDetailApiView, CarBrandApiView, CarBrandDetailApiView

urlpatterns = [
    path('brands/', CarBrandApiView.as_view()),
    path('brands/<int:pk>/', CarBrandDetailApiView.as_view()),
    path('cars/', CarApiView.as_view()),
    path('cars/<int:pk>/', CarDetailApiView.as_view()),
    path('cars/brand/<int:brand_id>/', CarApiView.as_view()),
]