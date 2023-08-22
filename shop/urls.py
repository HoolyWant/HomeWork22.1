from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop.views import home, contacts
from .apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>', views.NewDetailView.as_view(), name='product_info'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
