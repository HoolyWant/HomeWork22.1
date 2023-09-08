from django.contrib import admin
from shop.models import Product, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'buy_cost', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_title', 'version_number',)
    list_filter = ('product',)

