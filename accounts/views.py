from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse_lazy
from . import forms


class Signup(FormView):
    model = User
    form_class = forms.Usersignupform
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user.set_password(password)
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)


class Login(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    authentication_form = forms.Userloginform
    success_url = reverse_lazy('home')

class Home(View):
  def get(self,request):
    return  HttpResponse(f"hey {request.user.username}")