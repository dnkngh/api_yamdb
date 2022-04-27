from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APIGetToken,
    APISignup,
    CommentViewset,
    UsersViewSet,
    CategoryViewSet,
    GenreViewSet,
    ReviewViewset,
    TitleViewSet,
)

app_name = 'api'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
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
router.register(
    'users',
    UsersViewSet,
    basename='users'
)


urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
