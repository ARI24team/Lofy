from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import User
from . import forms
from django.http import HttpResponse
from django.core.mail import send_mail
from lofy.settings import EMAIL_HOST_USER


class Signup(FormView):
    model = User
    form_class = forms.Usersignupform
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the backend
            login(self.request, user)  # Log the user in
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

    # def form_valid(self, form):
    #     user = form.get_user()

    #     subject = "You've been logged in to lofy"
    #     message = f"Hey {user.username}, welcome back to your universe on LoFy!"
    #     from_email = EMAIL_HOST_USER
    #     recipient_list = [user.email]

    #     send_mail(subject, message, from_email, recipient_list, fail_silently=True)
    #     return super().form_valid(form)


def homeview(request):
    if request.user.is_authenticated:
        print(f"Logged-in user: {request.user.username}")
        return HttpResponse(f"Welcome back, {request.user.username}!")
    return HttpResponse("You're not logged in.")
