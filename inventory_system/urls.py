from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('stock.urls')),
    path('product-template/', include('product_template.urls')),
    path('product/', include('product.urls')),
]
