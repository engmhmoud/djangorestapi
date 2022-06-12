"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tickets.views import GuestViewset, guest_list, guest_pk, no_rest_no_model, no_rest_with_model

app_name = "tickets"
GuestViewsetRouter = DefaultRouter()
GuestViewsetRouter.register("", GuestViewset)

urlpatterns = [
    path("no_rest_no_model", no_rest_no_model, name="no_rest_no_model"),
    path("no_rest_with_model", no_rest_with_model, name="no_rest_with_model"),
    path("guest", guest_list, name="guest"),
    path("guest/<int:pk>", guest_pk, name="guest_pk"),
    path("guestviewset", include(GuestViewsetRouter.urls), name="guestviewset"),
]
