from django.shortcuts import render
from django.views.generic import DetailView

from shop.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'shop/home.html', context)


def contacts(request):
    return render(request, 'shop/contacts.html')


class NewDetailView(DetailView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'


