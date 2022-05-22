from django.contrib import admin
from .models import offer, product


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(offer, OfferAdmin )
admin.site.register(product, ProductAdmin  )

