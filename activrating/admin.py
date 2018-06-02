from django.contrib import admin

# Register your models here.

from .models import  Users, Activities




admin.site.register(Users )
admin.site.register(Activities)
