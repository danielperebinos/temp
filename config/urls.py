from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from config import settings

urlpatterns = [
    path(
        "api/v1/",
        include(
            [
                path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
                path("schema/", SpectacularAPIView.as_view(), name="schema"),
                path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
                path("institutions/", include("apps.institutions.urls")),
            ]
        ),
    ),
    path("", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
