from rest_framework.routers import DefaultRouter

from narguile.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()


router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = router.urls
