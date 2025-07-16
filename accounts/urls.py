from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_reset/', views.PasswordReset.as_view(), name='reset_password'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),

]
