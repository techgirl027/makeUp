from . import views
from django.urls import path

urlpatterns = [
    path("user/list", views.user_list),
    path("user/detail/<int:id>/", views.user_detail),
    path("service/list", views.service_list),
    path("service/detail/<int:id>/", views.service_detail),
    path("news/list", views.news_list),
    path("news/detail/<int:id>/", views.news_detail),
    path("comment/list", views.comment_list),
    path("comment/detail/<int:id>/", views.comment_detail),
    path("contact/list", views.contact_list),
    path("contact/detail/<int:id>/", views.contact_detail),
]
