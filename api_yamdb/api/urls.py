from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewset, ReviewViewset

router = DefaultRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewset,
    basename='comment'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewset,
    basename='reviews'
)

urlpatterns = [
    path('v1', include(router.urls)),
    path('v1', include('djoser.urls')),
    path('v1', include('djoser.urls.jwt'))
]
