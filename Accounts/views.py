from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from OnlineShoppingApp.models import Product
from .models import Customer
from OnlineShoppingApp.models import TodaysDeals,NewItems
from .forms import UserSignupForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":

            name = request.POST['user_name']
            email = request.POST['user_email']
            password = request.POST['user_password']
            confirm_password = request.POST['user_confirm_password']

            if password == confirm_password:
                if User.objects.filter(username=name).exists():
                    print ('username taken')
                elif User.objects.filter(email=email).exists():
                    print ('email taken')
                else:
                    user = User.objects.create_user(username=name,email=email,password=password)
                    user.save()
                    # customer_DOB = request.POST['user_name']
                    customer_gender = request.POST['user_password']
                    customer_address = request.POST['user_name']
                    customer_contact = request.POST['user_password']
                    profile = Customer(user=user ,customer_gender=customer_gender,
                                       customer_address=customer_address, customer_contact=customer_contact)
                    profile.save()

                    print ("users name and password")
                    print (user.customer.customer_contact)

                    return redirect('/Accounts/signin/')
    else:

        # user = User.objects.get(username='toney')
        # # # c = user.customer.customer_address
        # print (user.username.customer_address)
        return render(request, 'OnlineShoppingApp/signup.html')

def login(request):
    print ("working")
    data = Product.objects.all()
    TodaysDealsdata = TodaysDeals.objects.all()
    NewItemsdata = NewItems.objects.all()
    if request.method == "POST":
        login_name = request.POST['login_name']
        login_password = request.POST['login_password']

        user = auth.authenticate(username=login_name,password=login_password)
        print ("user =")
        print (user)
        print ("user id =")
        print (user.customer.customer_address)
        print(user.customer.customer_gender)
        if user is not None:
            auth.login(request,user)
            print(data)
            return redirect('/onlineshopping/', {"data": data, "TodaysDealsdata": TodaysDealsdata, "NewItemsdata":NewItemsdata})
        else:
            # message.info(request,'inavalid credentials')
            return render(request, 'OnlineShoppingApp/login.html')

    else:
        return render(request, 'OnlineShoppingApp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/Accounts/signin/')