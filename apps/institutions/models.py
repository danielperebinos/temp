from decimal import Decimal

from django.db import models

from apps.common.models import BaseModel


class Institution(BaseModel):
    # Base info
    name = models.CharField(max_length=255, help_text="The official name of the institution.")
    fields_of_professional_training = models.JSONField(
        default=dict, help_text="A JSON object listing the fields of professional training offered by the institution."
    )
    founding_authority = models.CharField(
        max_length=255, help_text="The authority or organization that founded the institution."
    )
    specialization = models.CharField(
        max_length=255, help_text="The main area of specialization or focus of the institution."
    )
    physical_address = models.CharField(
        max_length=255, help_text="The physical address of the institution, including street, city, and postal code."
    )

    # Contacts
    email = models.EmailField(
        max_length=255, blank=True, null=True, help_text="The official contact email address of the institution."
    )
    website = models.URLField(blank=True, null=True, help_text="The official website URL of the institution.")
    phone = models.CharField(
        max_length=255, blank=True, null=True, help_text="The contact phone number of the institution."
    )

    # Coords
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="The longitude coordinate of the institution's location.",
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="The latitude coordinate of the institution's location.",
    )

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ["name"]
        constraints = [models.UniqueConstraint(fields=["name", "physical_address"], name="unique_institution_address")]

    def __str__(self):
        return f"{self.name} [{self.physical_address}]"

    def get_coordinates(self) -> tuple[Decimal, Decimal]:
        if self.latitude and self.longitude:
            return self.latitude, self.longitude
