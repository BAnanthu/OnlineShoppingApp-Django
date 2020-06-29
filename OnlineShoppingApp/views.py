from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product
from .models import TodaysDeals,NewItems,AddToCart
# from .forms import UserSignupForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def home(request):
    data = Product.objects.all()
    TodaysDealsdata = TodaysDeals.objects.all()
    NewItemsdata = NewItems.objects.all()
    return render(request, 'OnlineShoppingApp/index.html', {"data": data, "TodaysDealsdata": TodaysDealsdata, "NewItemsdata":NewItemsdata})

# def register(request):
#     if request.method == "POST":
#
#             name =  request.POST['user_name']
#             email = request.POST['user_email']
#             password = request.POST['user_password']
#             confirm_password = request.POST['user_confirm_password']
#
#             if password == confirm_password:
#                 if User.objects.filter(username=name).exists():
#                     print ('username taken')
#                 elif User.objects.filter(email=email).exists():
#                     print ('email taken')
#                 else:
#                     user = User.objects.create_user(username=name,email=email,password=password)
#                     user.save()
#                     # customer_DOB = request.POST['user_name']
#                     customer_gender = request.POST['user_password']
#                     customer_address = request.POST['user_name']
#                     customer_contact = request.POST['user_password']
#                     profile = Customer(user=user ,customer_gender=customer_gender,
#                                        customer_address=customer_address, customer_contact=customer_contact)
#                     profile.save()
#
#                     print ("users name and password")
#                     print (user.customer.customer_contact)
#
#                     return render(request, 'OnlineShoppingApp/login.html')
#     else:
#
#         # user = User.objects.get(username='toney')
#         # # # c = user.customer.customer_address
#         # print (user.username.customer_address)
#         return render(request, 'OnlineShoppingApp/signup.html')

# def CustomerProfile(request):
#     if request.method == "POST":
#
#         customer_DOB = request.POST['customer_DOB']
#         customer_gender = request.POST['customer_gender']
#         customer_address = request.POST['customer_address']
#         customer_contact = request.POST['customer_contact']
#         profile = Customer(user=user,customer_DOB=customer_DOB, customer_gender=customer_gender, customer_address=customer_address,customer_contact=customer_contact)
#         profile.save()
#
#         return render(request, 'OnlineShoppingApp/index.html')
#
#     else:
#
#         # user = User.objects.get(username='toney')
#         # # # c = user.customer.customer_address
#         # print (user.username.customer_address)
#         return render(request, 'OnlineShoppingApp/CustomerProfile.html')

# def login(request):
#     print ("working")
#     data = Product.objects.all()
#     if request.method == "POST":
#         login_name = request.POST['login_name']
#         login_password = request.POST['login_password']
#
#         user = auth.authenticate(username=login_name,password=login_password)
#         print ("user =")
#         print (user)
#         print ("user id =")
#         print (user.customer.customer_address)
#         print(user.customer.customer_gender)
#         if user is not None:
#             auth.login(request,user)
#             return render(request, 'OnlineShoppingApp/index.html',{"data":data})
#         else:
#             # message.info(request,'inavalid credentials')
#             return render(request, 'OnlineShoppingApp/login.html')
#
#     else:
#         return render(request, 'OnlineShoppingApp/login.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return render(request,'OnlineShoppingApp/index.html')

def productDetails(request,product_id):
    product = Product.objects.get(product_id=product_id)
    return render(request, 'OnlineShoppingApp/product_details.html', {'product': product})

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
    return render(request, 'OnlineShoppingApp/mycart.html', {'mycart_items': mycart_items,'context':context})

def removeItem(request,cart_id):
    product = get_object_or_404(AddToCart, id=cart_id).delete()
    mycart_items = AddToCart.objects.filter(user=request.user)
    return render(request, 'OnlineShoppingApp/mycart.html', {'mycart_items': mycart_items})

def search(request):
    try:
        search = request.GET.get('search')
    except:
        search=None
    if search:
        products = Product.objects.filter(product_name__icontains=search)
        print(products)
        context = {'query': search, 'products': products}
        template = 'OnlineShoppingApp/search.html'
    else:
        context = {}
        template = 'OnlineShoppingApp/index.html'
    return render(request, template, context)