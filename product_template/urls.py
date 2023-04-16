from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductApiOverview, name='ProductApiOverview'),
    path('view-products/', views.showAllProducts, name='viewProducts'),
    path('create-product/', views.createProduct, name='createProduct'),
    path('update-product/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('delete-product/<int:pk>/', views.deleteProduct, name='deleteProduct'),

    path('ingredients/', views.IngredientApiOverview, name='IngredientApiOverview'),
    path('view-ingredients/', views.showAllIngredients, name='viewIngredients'),
    path('create-ingredient/', views.createIngredient, name='createIngredient'),
    path('update-ingredient/<int:pk>/', views.updateIngredient, name='updateIngredient'),
    path('delete-ingredient/<int:pk>/', views.deleteIgredient, name='deleteIngredient'),
]