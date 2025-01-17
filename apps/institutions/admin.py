from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.institutions.models import Institution


@admin.register(Institution)
class InstitutionAdmin(ModelAdmin):
    list_display = ("id", "name")
