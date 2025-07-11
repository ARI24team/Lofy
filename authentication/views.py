from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from . import forms
class Signup(CreateView):
    model=User
    form_class=forms.Usersignupform
    template_name='signup.html'
    success_url='/'
    def form_valid(self, form):
        password=form.cleaned_data['password']
        user=form.save()
        user.set_password(password)
        return super().form_valid(form)


