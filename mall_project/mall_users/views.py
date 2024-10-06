from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, LoginForm


def index(request):
    return render(request, 'index.html')


class RegisterView(FormView):
    template_name = 'registration.html'
    form_class = UserRegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'


