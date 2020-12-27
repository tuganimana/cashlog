from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('telephone','fullname','isverified','accounttype','password','created_at' ,'is_staff', 'is_active',)
    list_filter = ('telephone','fullname','isverified','accounttype','password','created_at', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('telephone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telephone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('telephone',)
    ordering = ('telephone',)


admin.site.register(CustomUser, CustomUserAdmin)