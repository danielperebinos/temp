from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


def environment_callback(_):
    environment = (settings.ENVIRONMENT or "development").lower()
    return {"production": ("production", "success"), "development": ("development", "warning")}.get(environment)


class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"}, status=200)
