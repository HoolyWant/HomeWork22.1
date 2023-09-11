from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verify')

    def form_valid(self, form):
        if form.is_valid():
            send_mail('Email verify',
                      f'Write this token {User.verify_token}',
                      'sir.saltickow@yandex.ru',
                      [User.email])
        form.save()
        return super().form_valid(form)


def verify_view(request):
    if request.method == 'POST':
        if request == User.verify_token:
            User.is_active = True

    return render(request, 'verify.html')



