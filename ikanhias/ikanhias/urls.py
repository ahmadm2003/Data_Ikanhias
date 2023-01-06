"""perpustakaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
from ikanhias_app.views import *
from django.conf import settings
from ikanhias_app.views import tambahikan_hias
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("halamandata/", halamandata, name='halamandata'),
    path("halamandata/", halamandata),
    path("halamanasal/", halamanasal),
    path("halamanharga/", halamanharga),
    path("halamandata/<int:id>", halamanaksi),
    path("tambahikanhias/", tambahikan_hias),
    path("halamandata/deleteikan_hias/<int:id_ikan_hias", deleteikan_hias, name="deleteikan_hias"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
]
