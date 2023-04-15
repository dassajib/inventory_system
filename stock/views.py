from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer

# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List': '/stock-list/',
        'Stock Detail': '/stock-detail/<int:id>/',
        'Create Stock': '/create-stock/',
        'Update Stock': '/update-stock/<int:id>/',
        'Delete Stock': 'delete-stock/<int:id>/',
    }

    return Response(api_urls);

@api_view(['GET'])
def showAllStocks(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewStock(request, pk):
    stock = Stock.objects.get(id=pk)
    serializer = StockSerializer(stock, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createStock(request):
    serializer = StockSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateStock(request, pk):
    stock = Stock.objects.get(id=pk)
    serializer = StockSerializer(instance=stock, data=request.data)

    if serializer.is_valid():
        serializer.save();
    
    return Response(serializer.data)

@api_view(['GET'])
def deleteStock(request, pk):
    stock = Stock.objects.get(id=pk)
    stock.delete()

    return Response("Stock deleted successfully.")

