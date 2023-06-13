from django.contrib import admin
from .models import Product, Offer, Registration
# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone' )


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Registration, RegistrationAdmin)