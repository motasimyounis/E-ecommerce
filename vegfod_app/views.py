from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.views.generic.list import ListView
from django.views.decorators.http import require_POST
from .models import Product
from django.views import View
from django.db.models import Q 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .forms import *
from django.utils import translation
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic



def signup(request): 
    if request.method == "POST":
        form = SignUpForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', "This email already exists.")
            else:
                form.save() 
                messages.add_message(request, messages.SUCCESS, 'Account has been successfully registered')
                return redirect('login') 
    else:
        form = SignUpForm()
    context = { 
        'form': form 
    } 
    return render(request, 'signup.html', context) 


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.add_message(request, messages.SUCCESS, 'ChangePassword is completed')

            return redirect('/')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'





# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm()
#     return render(request, 'profile.html', {'form': form})




def Index(request):
    return render(request,'index.html')


class ShopList(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'shop'
    ordering = ['id']
    paginate_by = 8
    # return render(request,'shop.html')




def Category(request,category):
    cate = get_object_or_404(Product,category=category)
    context = {
        'cate':cate
    }
    return render(request,'shop.html',context)

@login_required     
def Wishlist(request):
    user = request.user
    wishlist_items = WIshlist.objects.filter(user=user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def Single_product(request,name):
    single = get_object_or_404(Product,name=name)
    context = {
        'single':single
        
    }
    return render(request,'product-single.html',context)

@login_required     
def Carts(request):
    totalitem = 0
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    totalitem = len(cart_items)      

    if len(cart_items)== 0:
        cart_len= True
    else:
        cart_len=False  
    
    amount = 10
    tempamount = 0  
    af_dis = 0  
    dis =0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            
            if p.product.discount == 0 :
                tempamount = (p.quantity * p.product.price)
                amount = amount+tempamount    
            else:
                dis = p.quantity * p.product.discount
                af_dis = (p.product.price-p.product.discount)
                tempamount = (p.quantity * af_dis)
                amount = amount+tempamount  
            
    return render(request, 'cart.html', {'cart_items': cart_items,'cart_len':cart_len,'amount':amount,'tempamount':tempamount,'dis':dis,'totalitem':totalitem})


@login_required     
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)        
    cart = 0
    cart = Cart.objects.filter(user=user, product=product).exclude(quantity=0)
    if cart:
        cart = cart[0]
        cart.quantity += 1
        cart.save()
    else:
        cart = Cart.objects.create(user=user, product=product, quantity=1)
    messages.add_message(request, messages.SUCCESS, 'Added to cart successfully')
    return redirect('cart')
    

@login_required     
def deleteFromCart(request,id):
    if Cart.objects.get(pk=id):
        Cart.objects.filter(id=id).delete()
        messages.add_message(request, messages.SUCCESS, 'Deleted From cart successfully')
        return redirect('cart')


@login_required         
def deleteAllFRMCART(request):
    Cart.objects.all().delete()
    return redirect('cart')
    


@login_required     
def add_to_wishlist(request,product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    cart = WIshlist.objects.filter(user=user, product=product).exclude(quantity=0)
    if cart:
        cart = cart[0]
        cart.quantity += 1
        cart.save()
    else:
        cart = WIshlist.objects.create(user=user, product=product, quantity=1)
    messages.add_message(request, messages.SUCCESS, 'Added to wishlist successfully')
    return redirect('wishlist')

@login_required     
def deleteFromwishlist(request,id):
    if WIshlist.objects.get(pk=id):
        WIshlist.objects.filter(id=id).delete()
        messages.add_message(request, messages.SUCCESS, 'Deleted From wishlist successfully')
        return redirect('wishlist')

@login_required         
def deleteAllFRMwishlist(request):
    WIshlist.objects.all().delete()
    return redirect('wishlist')
    



   
def Check_out(request):
    totalitem = 0
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    totalitem = len(cart_items)      
    amount = 10
    tempamount = 0  
    af_dis = 0  
    dis =0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            
            if p.product.discount == 0 :
                tempamount = (p.quantity * p.product.price)
                amount = amount+tempamount    
            else:
                dis = p.quantity * p.product.discount
                af_dis = (p.product.price-p.product.discount)
                tempamount = (p.quantity * af_dis)
                amount = amount+tempamount  
    form = OrderForm()
    context = {
        'form':form,
        'amount':amount,
        'tempamount':tempamount,
        'dis':dis,
        'totalitem':totalitem
    }
    return render(request,'checkout.html',context)
