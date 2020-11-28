from rest_framework import routers
from .api import CVViewSet


router = routers.DefaultRouter()
router.register('api/todo', CVViewSet, 'cv')


urlpatterns = router.urls
