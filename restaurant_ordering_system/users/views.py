from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from users import forms
from users.models import User
from users.services import sendmail


class RegisterView(CreateView):  # регистрация, отправка запроса верификации на почту
    pass


class ConfirmPage(TemplateView):  # подтверждение почты
    pass


class ProfileView(UpdateView):
    pass
