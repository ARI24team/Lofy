from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetView,PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import User
from django.views import View
from . import forms
from django.http import HttpResponse
from django.core.mail import send_mail
from lofy.settings import EMAIL_HOST_USER
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
default_token_generator = PasswordResetTokenGenerator()
class Signup(FormView):
    model = User
    form_class = forms.Usersignupform
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the backend
            if user is not None:
                login(self.request, user)
                user.email_confirmed = False
                user.save()
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.id))
                url = f'http://{get_current_site(self.request).domain}/accounts/email_confirmtion/{uid}/{token}'
                subject = "You've been Sign up to lofy"
                message = f"Hey {user.username}, welcome to your universe on LoFy!,\n verfaiy its you\n {url} "
                from_email = EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)
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
class PasswordChange(PasswordChangeView):
    form_class=PasswordChangeForm
    template_name='accounts/password_change.html'
    success_url = reverse_lazy('accounts:home')

class PasswordReset(PasswordResetView):
    form_class=PasswordResetForm
    template_name='accounts/password_reset.html'
    from_email=EMAIL_HOST_USER
    success_url=reverse_lazy('accounts:password_reset_done')
    html_email_template_name='accounts/password_reset_email.html'

class PasswordResetDone(PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')

class PasswordResetComplete(PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'    

class Email_confirmtion(View):
  def get(self,request,uid,token):
    id=urlsafe_base64_decode(uid)
    try:
      user = User.objects.get(id=id)
    except Exception as e:
        user= None 
    if user and default_token_generator.check_token(user,token):    
      user.email_confirmed=True
      user.save()
      return HttpResponse("active")
    else :
      return HttpResponse("Not active there is an error")

