from django.db import models

# Create your models here.


class Users(models.Model):
    full_name = models.CharField(max_length=255)
    img = models.ImageField()
    bio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name


class Services(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.user.full_name


class News(models.Model):
    img = models.ImageField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
