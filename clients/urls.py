from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views import ClientViewSet

router = routers.SimpleRouter()
router.register(r'client', ClientViewSet)

urlpatterns = router.urls