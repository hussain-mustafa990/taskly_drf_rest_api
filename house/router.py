from rest_framework import routers

from .viewsets import HouseViewSet

app_name = "house"

router = routers.DefaultRouter()
router.register('houses', HouseViewSet)