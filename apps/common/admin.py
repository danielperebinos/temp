from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm
from unfold.forms import UserChangeForm as BaseUserChangeForm
from unfold.forms import UserCreationForm as BaseUserCreationForm

from apps.institutions.models import Institution

admin.site.unregister(User)
admin.site.unregister(Group)


class UserChangeForm(BaseUserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("user_permissions", None)


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("usable_password", None)
        self.fields["password1"].required = True
        self.fields["password2"].required = True


@admin.register(User)
class UnfoldUserAdmin(UserAdmin, ModelAdmin):
    list_display = ("username", "is_superuser", "first_name", "last_name")
    list_filter = ("is_superuser", "is_active", "groups")
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    readonly_fields = ("last_login", "date_joined")

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        content_type = ContentType.objects.get_for_model(Institution)
        permissions = Permission.objects.filter(content_type=content_type)
        super().save_model(request, obj, form, change)
        obj.user_permissions.add(*permissions)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
