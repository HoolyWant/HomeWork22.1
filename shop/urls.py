from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop.views import home, contacts

app_name = 'shop'

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
