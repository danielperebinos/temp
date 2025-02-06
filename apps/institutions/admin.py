from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from apps.institutions.models import Institution
from apps.institutions.resources import InstitutionResource


@admin.register(Institution)
class InstitutionAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = InstitutionResource
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_per_page = 20

    list_display = ("name", "type", "founding_authority", "physical_address")
    list_display_links = ("name", "type", "founding_authority", "physical_address")
    fieldsets = (
        ("General", {"fields": ("name", "founding_authority", "type", "physical_address")}),
        ("Summary", {"fields": ("summary", "description")}),
        ("Contacts", {"fields": ("email", "website", "phone")}),
        ("Coordinates", {"fields": ("longitude", "latitude")}),
        ("Track", {"fields": ("created_by", "created_at", "updated_by", "updated_at")}),
    )

    list_filter = (
        "type",
        "founding_authority",
        "created_by",
        "updated_by",
        ("created_at", RangeDateFilter),
        ("updated_at", RangeDateFilter),
    )
    search_fields = ("name", "description", "summary")
    search_help_text = "Search by name, description and summary occurencies"
    readonly_fields = ("created_by", "created_at", "updated_by", "updated_at")

    def get_resource_kwargs(self, request, *args, **kwargs):
        kwargs = super().get_resource_kwargs(request, *args, **kwargs)
        kwargs.update({"user": request.user})
        return kwargs

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)
