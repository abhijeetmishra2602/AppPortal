from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AndroidAppViewSet, UserTaskViewSet,admin_interface

router = DefaultRouter()
router.register(r'android-apps', AndroidAppViewSet)
router.register(r'user-tasks', UserTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_interface, name='admin_interface'),
]
