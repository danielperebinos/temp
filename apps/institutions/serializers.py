from rest_framework.serializers import ModelSerializer

from apps.institutions.models import Institution


class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        exclude = ("created_at", "updated_at", "created_by", "updated_by")
