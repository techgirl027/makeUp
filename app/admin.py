from django.contrib import admin
from app import models

# Register your models here.


admin.site.register(models.Users)
admin.site.register(models.News)
admin.site.register(models.Comments)
admin.site.register(models.Services)
admin.site.register(models.Contact)
