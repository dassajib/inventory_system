from django.contrib import admin
from .models import ProductTemplate, IngredientTemplate

# Register your models here.
admin.site.register(ProductTemplate)
admin.site.register(IngredientTemplate)
