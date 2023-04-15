from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name;
