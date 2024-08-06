from django.shortcuts import render
from app import models

# Create your views here.


def home_page(request):
    users = models.Users.objects.all()
    services = models.Services.objects.all()
    comments = models.Comments.objects.all()
    news = models.News.objects.all()
    context = {
        "users": users,
        "comments": comments,
        "services": services,
        "news": news,
    }
    return render(request, "lending/index.html", context)


def contact_page(request):
    contact = models.Contact.objects.all()
    context = {
        "contact": contact,
    }
    if request.method == "POST":
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        comment = request.POST["comment"]
        models.Contact.objects.create(
            email=email, full_name=first_name, phone=phone, comment=comment
        )
    return render(request, "lending/contact.html", context)
