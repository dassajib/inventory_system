from django.db import models

# Create your models here.
class ProductTemplate(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class IngredientTemplate(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)

    product = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name