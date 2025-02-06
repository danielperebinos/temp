from django import forms
from django.contrib import admin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from unfold.decorators import action

from apps.institutions.models import Institution
from apps.institutions.resources import InstitutionResource


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        widgets = {
            'description': WysiwygWidget(),
        }
        fields = '__all__'


@admin.register(Institution)
class InstitutionAdmin(ModelAdmin, ImportExportModelAdmin):
    # Import Export
    resource_class = InstitutionResource
    import_form_class = ImportForm
    export_form_class = ExportForm

    # Fields
    form = InstitutionForm
    fieldsets = (
        ("General", {"classes": ["tab"], "fields": ("name", "founding_authority", "type", "physical_address")}),
        ("Summary", {"classes": ["tab"], "fields": ("summary", "description")}),
        ("Contacts", {"classes": ["tab"], "fields": ("email", "website", "phone")}),
        ("Coordinates", {"classes": ["tab"], "fields": ("longitude", "latitude")}),
        ("Track", {"classes": ["tab"], "fields": ("created_by", "created_at", "updated_by", "updated_at")}),
    )

    # Display
    list_per_page = 20
    list_display = ("name", "type", "founding_authority", "physical_address")
    list_display_links = ("name", "type", "founding_authority", "physical_address")
    search_fields = ("name", "description", "summary")
    search_help_text = "Search by name, description and summary occurencies"
    readonly_fields = ("created_by", "created_at", "updated_by", "updated_at")
    list_filter_sheet = True
    list_filter_submit = True
    list_filter = (
        "type",
        "founding_authority",
        "created_by",
        "updated_by",
        ("created_at", RangeDateFilter),
        ("updated_at", RangeDateFilter),
    )

    # Actions
    actions_row = ["edit_row_action", "delete_row_action"]

    @action(
        description="Update Institution",
        url_path="update-institution-row-action",
    )
    def edit_row_action(self, request: HttpRequest, object_id: int):
        return redirect(
            reverse_lazy("admin:institutions_institution_change", args=[object_id])
        )

    @action(
        description="Delete Institution",
        url_path="delete-institution-row-action",
    )
    def delete_row_action(self, request: HttpRequest, object_id: int):
        return redirect(
            reverse_lazy("admin:institutions_institution_delete", args=[object_id])
        )

    def get_resource_kwargs(self, request: HttpRequest, *args, **kwargs):
        kwargs = super().get_resource_kwargs(request, *args, **kwargs)
        kwargs.update({"user": request.user})
        return kwargs

    def save_model(self, request: HttpRequest, obj, form, change):
        if obj.id is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)
