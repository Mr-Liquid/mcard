from django.contrib import admin

from .models import Product, Family, Transaction, Location

admin.site.register(Product)
admin.site.register(Family)
admin.site.register(Location)
admin.site.register(Transaction)

# Register your models here.
