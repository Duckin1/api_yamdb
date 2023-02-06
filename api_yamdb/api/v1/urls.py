from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, get_jwt_token,
                    sending_mail)

app_name = 'api'

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')
router.register('users', UserViewSet, basename='users')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', sending_mail),
    path('auth/token/', get_jwt_token, name='token'),
    path(
        'v1/auth/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
]
