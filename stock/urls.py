from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='ApiOverview'),
    path('view-stocks/', views.showAllStocks, name='viewStocks'),
    path('create-stock/', views.createStock, name='createStock'),
    path('update-stock/<int:pk>/', views.updateStock, name='updateStock'),
    path('delete-stock/<int:pk>/', views.deleteStock, name='deleteStock'),
]