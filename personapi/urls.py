from django.urls import include,path
from rest_framework import routers
from . import views

urlpatterns = [
    path('people/', views.CalculateInn.as_view(),  name='calculate_iin'),
    path('people/<str:iin>/', views.CalculateInn.as_view(), name='get_iin')
]