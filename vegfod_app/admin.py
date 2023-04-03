from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(orderplaced)
admin.site.register(WIshlist)

admin.site.site_title = 'E-commerce'
admin.site.site_header = 'E-commerce'