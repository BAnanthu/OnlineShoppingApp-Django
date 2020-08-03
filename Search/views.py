from django.shortcuts import render
from Products.models import Product
# Create your views here.
def search(request):
    try:
        search = request.GET.get('search')
    except:
        search=None
    if search:
        products = Product.objects.filter(product_name__icontains=search)
        context = {'query': search, 'products': products}
        template = 'OnlineShoppingApp/search.html'
    else:
        context = {}
        template = 'OnlineShoppingApp/index.html'
    return render(request, template, context)