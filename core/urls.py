from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homeview, name='home'),
    path('postcreation/', views.postcreationview, name="postcreation"),
]

