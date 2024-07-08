from django.db import models

# Products Models 

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES =((LIVE,'Live'),(DELETE,'Delete'))
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image =models.ImageField()
    priority = models.IntegerField(default=0) # priority to display product
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE) # to determine delete product or not
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # some of the standrad Practice

    def __str__(self) -> str:
        return self.title # string represention






