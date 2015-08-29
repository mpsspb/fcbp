from rest_framework import routers

from .views import CreditViewSet, PaymentViewSet


router = routers.SimpleRouter()
router.register(r'credits', CreditViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls