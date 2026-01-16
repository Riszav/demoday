from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path("register/", views.register),
    path("login/", views.login),
    path("admin/", admin.site.urls),
]
