from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from final_exam.accounts.forms import (
    LetUsTalkUserChangeForm,
    LetUsTalkUserCreationForm
)
from final_exam.accounts.models import LetUsTalkUser

UserModel = get_user_model()


# Register your models here.
@admin.register(LetUsTalkUser)
class LetUsTalkUserAdmin(UserAdmin):
    model = UserModel
    # add_form = LetUsTalkUserCreationForm
    # form = LetUsTalkUserChangeForm
    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
            (None, {'fields': ('email', 'password')}),
        #     ('Personal info', {'fields': ()}),
        #     ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        #     # ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
