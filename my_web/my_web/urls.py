from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from accounts.views import LoginView, register_page,  RegisterView, guest_register_view, login_page, log_out
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('register/guest', guest_register_view, name='guest_register'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', login_page, name='login'),
    path('logout', log_out , name='logout'),

]



