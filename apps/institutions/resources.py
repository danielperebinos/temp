import re

from import_export import fields
from import_export.resources import ModelResource
from import_export.widgets import CharWidget, Widget

from apps.institutions.models import Institution


def parse_coordinate(coordinate: str) -> float:
    coordinate = coordinate.strip(",")
    decimal_regex = r"^\s*(-?\d{1,3}[\.\,]\d+)\s*$"
    degree_regex = r"^\s*(\d{1,3})\s*°\s*(\d{1,2})\s*['′]\s*(\d{1,2}([.,]?\d+)?)\s*[″\"]?\s*([NSWE])?\s*$"

    if re.match(decimal_regex, coordinate):
        return float(coordinate.replace(",", "."))

    elif re.match(degree_regex, coordinate):
        match = re.match(degree_regex, coordinate)
        degrees = int(match.group(1))
        minutes = int(match.group(2))
        seconds = float(match.group(3).replace(",", ".")) if match.group(3) else 0.0
        direction = match.group(5)
        decimal_coordinate = degrees + (minutes / 60) + (seconds / 3600)

        if direction in ["S", "W"]:
            decimal_coordinate *= -1

        return decimal_coordinate

    raise ValueError("Value could not be parsed using defined formats.")


class CoordinateWidget(Widget):
    def clean(self, value, row=None, *args, **kwargs):
        return parse_coordinate(str(value))


class InstitutionResource(ModelResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs.get("user")

    name = fields.Field(column_name="Instituția de învățământ profesional tehnic", attribute="name")
    type = fields.Field(column_name="Tipul institutiei", attribute="type")
    founding_authority = fields.Field(column_name="Fondator", attribute="founding_authority")
    physical_address = fields.Field(
        column_name="Adresa juridică, inclusiv pentru sediile arondate", attribute="physical_address"
    )
    email = fields.Field(column_name="E-email", attribute="email")
    website = fields.Field(column_name="Pagina web", attribute="website")
    phone = fields.Field(column_name="Telefon director / anticameră", attribute="phone")
    summary = fields.Field(column_name="Inst summary", attribute="summary")
    description = fields.Field(column_name="Description", attribute="description", widget=CharWidget())
    latitude = fields.Field(column_name="Latitudine", attribute="latitude", widget=CoordinateWidget())
    longitude = fields.Field(column_name="Longitudine", attribute="longitude", widget=CoordinateWidget())

    class Meta:
        model = Institution
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ("name",)
        fields = (
            "name",
            "type",
            "founding_authority",
            "physical_address",
            "email",
            "website",
            "phone",
            "summary",
            "description",
            "latitude",
            "longitude",
        )

    def skip_row(self, instance, original, row, import_validation_errors=None):
        print("Skipping row")
        return not any(row.values())

    def before_import_row(self, row, **kwargs):
        keys = list(row.keys())
        for key in keys:
            new_key = key.strip() if isinstance(key, str) else key
            value = row[key].strip() if isinstance(row[key], str) else row[key]
            row.pop(key, None)
            row[new_key] = value

    def before_save_instance(self, instance, row, **kwargs):
        if instance.id is None:
            instance.created_by = self.user

        instance.updated_by = self.user
