from django.shortcuts import render,redirect,get_object_or_404
from Products.models import Product
from .models import Orders
import datetime
# Create your views here.

def Order(request,product_id):
    if request.method == "POST":
        payment_method = request.POST['payment']
        product = Product.objects.get(product_id=product_id)
        date=datetime.datetime.now().date()
        product_price = product.product_dealprice
        shipping_charge = 45
        user_id = request.user.id

        Orders_instance = Orders.objects.create(
            user=request.user,
            product=product,
            order_customer_id=user_id,
            order_date=date,
            order_delivery_date= date + datetime.timedelta(days=3),
            order_shipping_charge=shipping_charge,
            order_deal_price=product_price + shipping_charge,
            order_payment_method=payment_method,
        )

        return redirect('/onlineshopping/')

def removeOrderItem(request,order_id):
    product = get_object_or_404(Orders, order_id=order_id).delete()
    myorder_items = Orders.objects.filter(user=request.user)

    return render(request, 'OnlineShoppingApp/myOrders.html', {'myorder_items': myorder_items})


def myOrders(request):
    myorder_items = Orders.objects.filter(user=request.user);
    return render(request, 'OnlineShoppingApp/myOrders.html', {'myorder_items': myorder_items})