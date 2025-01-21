from rest_framework.serializers import DecimalField, ListSerializer, ModelSerializer

from apps.institutions.models import Institution


class InstitutionSerializer(ModelSerializer):
    coordinates = ListSerializer(
        child=DecimalField(max_digits=13, decimal_places=10), min_length=2, max_length=2, allow_empty=False
    )

    class Meta:
        model = Institution
        exclude = ("created_at", "updated_at", "created_by", "updated_by", "latitude", "longitude")
