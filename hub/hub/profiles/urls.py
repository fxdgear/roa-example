from rest_framework import routers

from profiles.api import DockerUserViewSet

router = routers.SimpleRouter()
router.register(r'users', DockerUserViewSet)
urlpatterns = router.urls
