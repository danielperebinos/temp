from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from apps.common.models import BaseModel


class InstitutionType(models.TextChoices):
    CENTRUL_DE_EXCELENTA = "Centrul de Excelenţă", "Centrul de Excelenţă"
    COLEGIUL = "Colegiul", "Colegiul"
    SCOALA_PROFESIONALA = "Școala Profesională", "Școala Profesională"


class Institution(BaseModel):
    # Base info
    name = models.CharField(
        max_length=255,
        verbose_name="Instituția de învățământ profesional tehnic",
        help_text="The official name of the institution."
    )
    type = models.CharField(
        max_length=255,
        choices=InstitutionType.choices,
        verbose_name="Tipul institutiei",
        help_text="The type of the institution."
    )
    founding_authority = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Fondator",
        help_text="The authority or organization that founded the institution."
    )
    physical_address = models.CharField(
        max_length=255,
        verbose_name="Adresa juridică, inclusiv pentru sediile arondate",
        help_text="The physical address of the institution, including street, city, and postal code."
    )

    # Contacts
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="E-email",
        help_text="The official contact email address of the institution."
    )
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name="Pagina web",
        help_text="The official website URL of the institution."
    )
    phone = models.CharField(
        max_length=255,
        validators=[RegexValidator(r"^([\d\s\W]+)(,\s[\d\s\W]+)*$")],
        verbose_name="Telefon director / anticameră",
        help_text="The contact phone number of the institution."
    )
    summary = models.TextField(
        verbose_name="Inst summary",
        help_text="A brief summary of the institution's key details."
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Description",
        help_text="Optional rich text providing detailed information about the institution, such as specialties and study duration.",
    )

    # Coords
    longitude = models.DecimalField(
        max_digits=13,
        decimal_places=10,
        blank=True,
        null=True,
        validators=[MinValueValidator(Decimal(-180)), MaxValueValidator(Decimal(180))],
        verbose_name="Longitudine",
        help_text="The longitude coordinate of the institution's location.",
    )
    latitude = models.DecimalField(
        max_digits=13,
        decimal_places=10,
        blank=True,
        null=True,
        validators=[MinValueValidator(Decimal(-90)), MaxValueValidator(Decimal(90))],
        verbose_name="Latitudine",
        help_text="The latitude coordinate of the institution's location.",
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="institutions_created",
        verbose_name="Creat de",
        help_text="The user who created the institution.",
    )

    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="institutions_updated",
        verbose_name="Actualizat de",
        help_text="The user who updated the institution.",
    )

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ["name"]
        constraints = [models.UniqueConstraint(fields=["name", "physical_address"], name="unique_institution_address")]

    def __str__(self):
        return self.name

    @property
    def coordinates(self):
        return self.latitude, self.longitude
