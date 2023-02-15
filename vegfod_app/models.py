from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser, Permission, Group

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     groups = models.ManyToManyField(Group, related_name='vegfod_app_groups')
#     user_permissions = models.ManyToManyField(Permission, related_name='vegfod_app_user_permissions')


class Product(models.Model):
    choices= [
        ('Vegetables','Vegetables'),
        ('Fruits','Fruits'),
        ('Juice','Juice'),
        ('Dried','Dried'),
    ]
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount  = models.FloatField(blank=True,null=True,default=0)
    image = models.ImageField() 
    category = models.CharField(choices=choices,max_length=50)
    description = models.TextField()

    
    def __str__(self):
        return self.name
    
    @property
    def rate(self):
        return int( (self.discount / self.price)*100)
    @property
    def af_price(self):
        return int( self.price - self.discount)
    
State_Choices=(
        ('Gaza','Gaza'),
        ('Nusirate','Nusirate'),
        ('Alzhra','Alzhra'),
        ('Rafah','Rafah'),
    )
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=State_Choices,max_length=50)
    addrees1 = models.TextField(max_length=250,default='such as: Salah_aldeen- in nuserate')
    addrees2 = models.TextField(max_length=250,blank=True,null=True)
    
    def __str__(self):
        return str(self.id)
    @property
    def username(self):
        return self.user
    
    
class orderplaced(models.Model):
    Status_Choices=(
        ('Accepted','Accepted'),
        ('Packed','Packed'),
        ('On The Way','On The Way'),
        ('Delivered','Delivered'),
        ('Cancel','Cancel'),
    )
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)    
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices= Status_Choices,default='Pending',max_length=50 ) 
    
    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def __str__(self):
        return str(self.id) 
        
class WIshlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id) 
        


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
