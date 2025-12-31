from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Information personnelles', {
            'fields': (
                # 'first_name', 
                # 'last_name', 
                # 'email', 
                'phone_number', 
                'profile_picture'
            ),
        }),
        ('Rôle', {
            'fields': ('role',),    
        }),
    )

    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Informations personnelles', {
    #         'fields': (
    #             'first_name',
    #             'last_name',
    #             'email',
    #             'phone_number',
    #             'profile_picture',
    #         ),
    #     }),
    #     ('Permissions', {
    #         'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     ('Dates importantes', {
    #         'fields': ('last_login', 'date_joined'),
    #     }),
    # )

    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

admin.site.register(User, CustomUserAdmin)
