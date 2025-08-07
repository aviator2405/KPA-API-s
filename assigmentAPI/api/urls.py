from django.contrib import admin
from django.urls import path
from api.views import WheelSpecificationView, WheelSpecificationFilterView


urlpatterns = [
    # Wheel Specification Entry API
    path('wheel-specifications/', WheelSpecificationView.as_view(), name='wheel-specifications'),
    # Filteration API 
    path('wheel-specifications/filter/', WheelSpecificationFilterView.as_view(), name='wheel-specifications-filter'),
]
