from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm
class Usersignupform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

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

    
    