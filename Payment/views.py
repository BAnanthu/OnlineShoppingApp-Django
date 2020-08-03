from django.shortcuts import render

# Create your views here.
def PaymentMethods(request,product_id):
    return render(request, 'OnlineShoppingApp/payment-method.html', {'product_id': product_id})

