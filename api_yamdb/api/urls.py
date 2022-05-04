from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewset, GenreViewSet,
                    ReviewViewset, TitleViewSet, UsersViewSet, signup, token)

app_name = 'api'

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewset,
    basename='comments'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewset,
    basename='reviews'
)
router.register(
    'users',
    UsersViewSet,
    basename='users'
)

v1_patterns = [
    path('auth/token/', token, name='get_token'),
    path('', include(router.urls)),
    path('auth/signup/', signup, name='signup'),
]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]
