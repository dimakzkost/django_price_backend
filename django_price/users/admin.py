from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'full_name', 'IIN', 'phone', 'status']

    fieldsets = UserAdmin.fieldsets + (
        ('Реквизиты клиента', {'fields': ('status', 'full_name', 'IIN', 'phone', 'delivery_adress', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Реквизиты клиента', {'fields': ('status', 'full_name', 'IIN', 'phone', 'delivery_adress', )}),
    )

    search_fields = ('full_name', 'username', 'IIN')
    ordering = ('full_name', 'username',)
    list_filter = ('status', )


admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
