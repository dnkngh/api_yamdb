from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APIGetToken,
    APISignup,
    UsersViewSet,
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
)

app_name = 'api'

router = router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)

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
