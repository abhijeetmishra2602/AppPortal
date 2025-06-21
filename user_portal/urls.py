from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, TaskViewSet,user_interface

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('user/', user_interface, name='user_interface'),
    path('', include(router.urls)),
]
