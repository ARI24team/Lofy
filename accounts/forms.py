from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
class Usersignupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'Phone_Number','password1','password2']
    def __init__(self, *args, **kwargs):
        super(Usersignupform,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter Username',
            'class': 'form-control'
        })
        super(Usersignupform,self).__init__(*args, **kwargs)
        self.fields['Phone_Number'].widget.attrs.update({
            'placeholder': 'Phone Number',
            'class': 'form-control',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter Your Email',
            'class': 'form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confierm your password',
            'class': 'form-control'
        })


class Userloginform(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(Userloginform, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control'
        })

    
    