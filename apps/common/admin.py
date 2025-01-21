from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from apps.institutions.models import Institution

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UnfoldUserAdmin(UserAdmin, ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ("is_superuser", "is_active", "groups")
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        content_type = ContentType.objects.get_for_model(Institution)
        permissions = Permission.objects.filter(content_type=content_type)
        super().save_model(request, obj, form, change)
        obj.user_permissions.add(*permissions)


@admin.register(Group)
class UnfoldGroupAdmin(GroupAdmin, ModelAdmin):
    pass
