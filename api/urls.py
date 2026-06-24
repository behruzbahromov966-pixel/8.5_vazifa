from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (CarBrandViewSet, CarViewSet, CommentViewSet)

router = SimpleRouter()
router.register('cars', CarViewSet)
router.register("brands",CarBrandViewSet)
router.register("comments", CommentViewSet)



urlpatterns = [
    path("", include(router.urls)),
    # path('brands/', CarBrandApiView.as_view()),
    # path('brands/<int:pk>/', CarBrandDetailApiView.as_view()),
    # path('cars/', CarApiView.as_view()),
    # path('cars/<int:pk>/', CarDetailApiView.as_view()),
    path('cars/brand/<int:brand_id>/', CarViewSet.as_view({"get": "list"})),
    # path('cars/<int:pk>/comments/', CommentApiView.as_view()),
    # path('cars/<int:pk>/comments/<int:pk>/', CommentDetailApiView.as_view()),
]