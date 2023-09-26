from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import UserUser

@admin.register(UserUser)
class UserAdmin(BaseUserAdmin):
    pass

# Register your models here.
