from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/<str:meal_type>/', views.menu, name='menu'),
]
