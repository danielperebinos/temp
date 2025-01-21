from django.contrib.auth.models import User
from django.db import models

from apps.common.models import BaseModel


class Institution(BaseModel):
    # Base info
    name = models.CharField(max_length=255, help_text="The official name of the institution.")
    type = models.CharField(max_length=255, help_text="The type of the institution.")
    founding_authority = models.CharField(
        max_length=255, blank=True, default="", help_text="The authority or organization that founded the institution."
    )
    physical_address = models.CharField(
        max_length=255, help_text="The physical address of the institution, including street, city, and postal code."
    )

    # Contacts
    email = models.EmailField(
        max_length=255, blank=True, null=True, help_text="The official contact email address of the institution."
    )
    website = models.URLField(blank=True, null=True, help_text="The official website URL of the institution.")
    phone = models.CharField(max_length=255, help_text="The contact phone number of the institution.")
    summary = models.TextField(help_text="A brief summary of the institution's key details.")
    description = models.TextField(
        blank=True,
        default="",
        help_text="Optional rich text providing detailed information about the institution, such as specialties and study duration.",
    )

    # Coords
    longitude = models.DecimalField(
        max_digits=13,
        decimal_places=10,
        blank=True,
        null=True,
        help_text="The longitude coordinate of the institution's location.",
    )
    latitude = models.DecimalField(
        max_digits=13,
        decimal_places=10,
        blank=True,
        null=True,
        help_text="The latitude coordinate of the institution's location.",
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="institutions_created",
        help_text="The user who created the institution.",
    )

    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="institutions_updated",
        help_text="The user who updated the institution.",
    )

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ["name"]
        constraints = [models.UniqueConstraint(fields=["name", "physical_address"], name="unique_institution_address")]

    def __str__(self):
        return f"{self.name} [{self.physical_address}]"

    @property
    def coordinates(self):
        return self.latitude, self.longitude
