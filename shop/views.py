from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (DetailView, ListView,
                                  CreateView, UpdateView, DeleteView)
from pytils.translit import slugify

from shop.forms import ProductForm, VersionForm
from shop.models import Product, Blog, Version


class ProductListView(ListView):
    model = Product


def contacts(request):
    return render(request, 'shop/contacts.html')


class ProductView(DetailView):
    model = Product


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)



class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:product_list')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(activity_sign=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('shop:blog_view', args=[self.kwargs.get('pk')])


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'activity_sign')
    success_url = reverse_lazy('shop:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
            return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('shop:blog_list')





