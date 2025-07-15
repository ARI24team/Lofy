from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeview, name='home'),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
]
