from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_updated_by")

    class Meta:
        abstract = True
