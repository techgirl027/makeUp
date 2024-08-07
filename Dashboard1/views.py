from django.shortcuts import render
from app import models


def index(request):
    return render(request, "dashboard/index.html")


def contactList(request):
    contacts = models.Contact.objects.all()
    context = {"contacts": contacts}
    return render(request, "dashboard/list.html", context)


def login(request):
    # if request.method == "POST":
    # email = request.POST["email"]
    # password = request.POST["password"]
    return render(request, "dashboard/login.html")
