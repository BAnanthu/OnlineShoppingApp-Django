from django.shortcuts import render,get_object_or_404,redirect
from Products.models import Product
from .models import AddToCart


# Create your views here.

def addToCart(request,product_id):
    product = get_object_or_404(Product,product_id=product_id)
    cart_added_product, created= AddToCart.objects.get_or_create(user=request.user,product=product)
    mycart_items = AddToCart.objects.filter(user=request.user)
    print(cart_added_product)
    if not created:
        if AddToCart.objects.filter(product_id=product.product_id,user=request.user).exists():

            order_qs=AddToCart.objects.filter(product_id=product.product_id,user=request.user)
            order = order_qs[0]
            order.quantity += 1
            order.save()
            context = "true"
    return redirect(myCart)

def removeItem(request,cart_id):
    product = get_object_or_404(AddToCart, id=cart_id).delete()
    mycart_items = AddToCart.objects.filter(user=request.user)
    return render(request, 'OnlineShoppingApp/mycart.html', {'mycart_items': mycart_items})


def myCart(request):
    mycart_items = AddToCart.objects.filter(user=request.user);
    return render(request, 'OnlineShoppingApp/mycart.html', {'mycart_items': mycart_items})