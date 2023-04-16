from rest_framework import serializers
from .models import ProductTemplate,IngredientTemplate

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientTemplate
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProductTemplate
        fields = '__all__'