from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import User
from . import forms


class Signup(FormView):
    model = User
    form_class = forms.Usersignupform
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(Signup, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)


class Login(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    authentication_form = forms.Userloginform
    success_url = '/'