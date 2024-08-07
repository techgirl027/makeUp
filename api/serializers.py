from rest_framework.serializers import ModelSerializer
from app.models import Users, Services, News, Comments, Contact


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class NewSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
