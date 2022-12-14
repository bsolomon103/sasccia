"""sasccia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from home import views
from django.views.generic import TemplateView
from clients.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('clients/', include('clients.urls')),
    path('', include('frontend.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth', include('rest_framework.urls')),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
   
    ]

urlpatterns += [re_path('.*', TemplateView.as_view(template_name='index.html'))]



