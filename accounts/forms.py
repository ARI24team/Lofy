from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class Usersignupform(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'Phone_Number', 
            'password1', 
            'password2'
            ]
        
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Youremail@example.com'})
        }

    def __init__(self, *args, **kwargs):
        super(Usersignupform, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter Username',
            'class': 'form-control'
        })
        self.fields['Phone_Number'].widget.attrs.update({
            'placeholder': 'Phone Number',
            'class': 'form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm your password',
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
        for field in self.fields.values():
            field.help_text = ''
