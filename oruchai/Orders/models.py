from django.db import models
from Customers.models import Customer
from Produts.models import Product
# Orders Model

class Cart(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES =((LIVE,'Live'),(DELETE,'Delete'))
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE) # to determine delete product or not
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # some of the standrad Practice

class CartItem(models.Model):
    product = models.ForeignKey()
