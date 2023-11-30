from django.urls import include, path
from rest_framework import routers
from . import views as api_views

router = routers.DefaultRouter()
router.register(r'', api_views.HomeViewSet)
router.register('video/(?P<link>[^/.]+)', api_views.VideoViewSet, basename="video-details")
router.register(r'comments', api_views.CommentModelViewSet, basename="post-list")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls