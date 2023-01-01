# from dataclasses import fields
from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'password')
    search_fields = ('first_name', 'last_name','email','password')

admin.site.register(User, UserAdmin)

