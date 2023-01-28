from django.urls import path

from .views import (get_jwt_token, register)


urlpatterns = [
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
