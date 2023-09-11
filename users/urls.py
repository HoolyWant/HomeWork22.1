from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, verify_view

app_name = UsersConfig.name

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('verify/', verify_view, name='verify')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

