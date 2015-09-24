from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls
