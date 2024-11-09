from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vehiculo, CustomUser

admin.site.register(Vehiculo)

class CustomUserAdmin(UserAdmin):
    model= CustomUser
    list_display=['username','email','is_staff', 'is_active']

#Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
