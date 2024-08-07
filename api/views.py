from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    ContactSerializer,
    CommentSerializer,
    NewSerializer,
    ServiceSerializer,
)
from app.models import Users, Comments, Contact, News, Services


@api_view(["GET"])
def user_list(request):
    users = Users.objects.all()
    ser_data = UserSerializer(users, many=True)
    return Response(ser_data.data)


@api_view(["GET"])
def user_detail(request, id):
    user = Users.objects.get(id=id)
    ser_data = UserSerializer(user)
    return Response(ser_data.data)


@api_view(["GET"])
def service_list(request):
    services = Services.objects.all()
    ser_data = ServiceSerializer(services, many=True)
    return Response(ser_data.data)


@api_view(["GET"])
def service_detail(request, id):
    services = Services.objects.get(id=id)
    ser_data = ServiceSerializer(services)
    return Response(ser_data.data)


@api_view(["GET"])
def news_list(request):
    news = News.objects.all()
    ser_data = NewSerializer(news, many=True)
    return Response(ser_data.data)


@api_view(["GET"])
def news_detail(request, id):
    news = News.objects.get(id=id)
    ser_data = NewSerializer(news)
    return Response(ser_data.data)


@api_view(["GET"])
def comment_list(request):
    comments = Comments.objects.all()
    ser_data = CommentSerializer(comments, many=True)
    return Response(ser_data.data)


@api_view(["GET"])
def comment_detail(request, id):
    comments = Comments.objects.get(id=id)
    ser_data = CommentSerializer(comments)
    return Response(ser_data.data)


@api_view(["GET"])
def contact_list(request):
    contacts = Contact.objects.all()
    ser_data = ContactSerializer(contacts, many=True)
    return Response(ser_data.data)


@api_view(["GET"])
def contact_detail(request, id):
    contacts = Contact.objects.get(id=id)
    ser_data = ContactSerializer(contacts)
    return Response(ser_data.data)
