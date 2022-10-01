from rest_framework.routers import SimpleRouter
from .views import StorageViewset
router = SimpleRouter()
router.register('images', StorageViewset)
urlpatterns = router.urls