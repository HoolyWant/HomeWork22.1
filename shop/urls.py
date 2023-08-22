from django.contrib import admin
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', 'shop.urls', name='shop')
]
