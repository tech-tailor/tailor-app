from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from .models import CustomUserGroup


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('User Information', {
            'fields': ('username', 'email', 'phone_number', 'password', 'verified', 'verify_code')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
      
    list_display = ('username', 'phone_number', 'email', 'verified', 'is_staff')  # Add 'phone' here
    
    list_filter = ('is_active', 'is_staff', 'groups')
    search_fields = ('username', 'email', 'phone', 'phone_number')
    ordering = ('-date_joined',)
    date_hierarchy = 'date_joined'
    
    
    
class CustomUserGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


    
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserGroup, CustomUserGroupAdmin)