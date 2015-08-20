from rest_framework import routers

from .views import CreditViewSet


router = routers.SimpleRouter()
router.register(r'credits', CreditViewSet)

urlpatterns = router.urls