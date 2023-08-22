from django.contrib import admin
from shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'buy_cost', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)
