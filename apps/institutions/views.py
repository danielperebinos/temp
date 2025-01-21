from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.institutions.models import Institution
from apps.institutions.serializers import InstitutionSerializer


class InstitutionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    pagination_class = None
