from rest_framework.routers import SimpleRouter

from apps.institutions.views import InstitutionViewSet

router = SimpleRouter()
router.register("", InstitutionViewSet)

urlpatterns = router.urls
