from rest_framework.routers import DefaultRouter

from app_people.views import PersonViewSet, PersonViewSetAlt

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
# router.register(r'persons', PersonViewSetAlt)

urlpatterns = router.urls