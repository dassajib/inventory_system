from rest_framework import serializers
from .models import Product, Ingredient
from product_template.serializers import IngredientSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ingredient
        fields = '__all__'