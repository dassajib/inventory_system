from django.db import models
from product_template.models import IngredientTemplate

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    price = models.IntegerField(default=0)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredientTemplate = models.OneToOneField(IngredientTemplate, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return str(self.price)
