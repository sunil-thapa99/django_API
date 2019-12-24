from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomerUser

# Register your models here.
admin.site.register(CustomerUser)
# admin.site.register(UserProfile)
