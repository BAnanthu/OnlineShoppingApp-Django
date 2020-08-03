from django.shortcuts import render
from .models import Product

# Create your views here.
def productDetails(request,product_id):
    product = Product.objects.get(product_id=product_id)
    return render(request, 'OnlineShoppingApp/product_details.html', {'product': product})