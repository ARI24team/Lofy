
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import User
from . import forms

class Signup(CreateView):
    model = User
    form_class = forms.Usersignupform
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form):
        password = form.cleaned_data['password1']
        user = form.save()
        user.set_password(password)
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)


class Login(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    authentication_form = forms.Userloginform
    success_url = '/'