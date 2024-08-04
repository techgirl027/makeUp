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
