from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.Index , name='index'),
    path('signup',views.signup, name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('cart',views.Carts,name='cart'),
    path('shop',views.ShopList.as_view() , name='shop'),
    path('shop/<str:category>/', views.Category, name='category'),
    path('wishlist',views.Wishlist ,name='wishlist'),
    path('product/<str:name>',views.Single_product,name='product-single'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:id>', views.deleteFromCart, name='delete_from_cart'),
    path('deleteAllFRMCART',views.deleteAllFRMCART , name='deleteAllFRMCART'),
    path('delete_from_wishlist/<int:id>', views.deleteFromwishlist, name='delete_from_wishlist'),
    path('deleteAllFRMwishlist',views.deleteAllFRMwishlist , name='deleteAllFRMwishlist'),
    path('add_to_wishlist/<int:product_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('checkout',views.Check_out,name='checkout'),
    path('change_password/',views.change_password, name='change_password'),
    


]