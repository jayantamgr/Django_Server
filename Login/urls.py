from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, createUserViewSet, UserViewSet
from . import views
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('person', PersonViewSet, basename='person')
router.register('createuser', createUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api/auth/', include('knox.urls')),
]
