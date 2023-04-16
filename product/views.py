from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Ingredient
from .serializers import ProductSerializer, IngredientSerializer

# Create your views here.
@api_view(['GET'])
def ProductApiOverview(request):
    product_api_urls = {
        'List': '/product-list/',
        'Product Detail': '/product-detail/<int:id>/',
        'Create Product': '/create-product/',
        'Update Product': '/update-product/<int:id>/',
        'Delete Product': 'delete-product/<int:id>/',
    }

    return Response(product_api_urls);

@api_view(['GET'])
def showAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save();
    
    return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response("Product deleted successfully.")



# Ingredient Api
@api_view(['GET'])
def IngredientApiOverview(request):
    ingredient_api_urls = {
        'List': '/ingredient-list/',
        'Ingredient Detail': '/ingredient-detail/<int:id>/',
        'Create Ingredient': '/create-ingredient/',
        'Update Ingredient': '/update-ingredient/<int:id>/',
        'Delete Ingredient': 'delete-ingredient/<int:id>/',
    }

    return Response(ingredient_api_urls);

@api_view(['GET'])
def showAllIngredient(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewIngredient(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    serializer = ProductSerializer(ingredient, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createIngredient(request):
    serializer = IngredientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateIngredient(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    serializer = IngredientSerializer(instance=ingredient, data=request.data)

    if serializer.is_valid():
        serializer.save();
    
    return Response(serializer.data)

@api_view(['GET'])
def deleteIngredient(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    ingredient.delete()

    return Response("Ingredient deleted successfully.")