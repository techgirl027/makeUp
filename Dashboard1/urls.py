from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard_index"),
    path("contact/", views.contactList, name="contactList"),
    path("login/", views.login, name="login"),
]
