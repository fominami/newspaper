from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm 
from django.contrib.auth.views import LogoutView, LoginView

class logout_view(LogoutView):
    success_url=reverse_lazy('home')


class login_view(LoginView):
    template_name = 'registration/login.html'
    '''success_url=reverse_lazy('home')'''


class SignUp(generic.CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'
