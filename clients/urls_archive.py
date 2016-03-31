from django.conf.urls import patterns, include, url

from rest_framework import routers

from .views_archive import ClientClubCardViewSet


router = routers.SimpleRouter()

router.register(r'clubcard', ClientClubCardViewSet, 'ClubCard')

urlpatterns = router.urls
