from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'api/v1/users', CustomUserViewSet, basename='users')
router.register(r'api/v1/user', ProfileCustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/user_logout/', LogoutView.as_view(), name='user_logout')

]
