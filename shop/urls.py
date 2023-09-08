from .apps import ShopConfig
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop.views import (contacts, ProductView, ProductListView, BlogListView,
                        BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreate, ProductUpdate,
                        ProductDelete)


app_name = ShopConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>', ProductView.as_view(), name='product_info'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='blog_edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('create_product/', ProductCreate.as_view(), name='product_create'),
    path('edit_product/<int:pk>', ProductUpdate.as_view(), name='product_edit'),
    path('delete_product/<int:pk>', ProductDelete.as_view(), name='product_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
