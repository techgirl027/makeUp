from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.home_page, name="index"),
    path("contact/", views.contact_page, name="contact_page"),
]
