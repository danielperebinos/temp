from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creat"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Actualizat"
    )

    class Meta:
        abstract = True
