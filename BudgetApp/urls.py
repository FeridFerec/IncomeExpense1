from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('main/', views.main,name='main'),
    path('main/income/', views.income,name='income'),
    path('main/expenses/', views.expenses,name='expenses'),
]