from django.urls import include, path
from rest_framework import routers
from . import views as api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)

router = routers.DefaultRouter()
router.register(r'', api_views.HomeViewSet)
router.register('video/(?P<link>[^/.]+)', api_views.VideoViewSet, basename="video-details")
router.register(r'comments', api_views.CommentModelViewSet, basename="post-list")
router.register('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
router.register('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
router.register('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
router.register('blacklist/', TokenBlacklistView.as_view(), name='token_blacklist')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls