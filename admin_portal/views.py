from rest_framework import viewsets, permissions
from .models import AndroidApp, UserTask
from .serializers import AndroidAppSerializer, UserTaskSerializer
from django.shortcuts import render

def admin_interface(request):
    return render(request, 'admin_portal/admin_interface.html')

class AndroidAppViewSet(viewsets.ModelViewSet):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer
    permission_classes = [permissions.IsAdminUser]

class UserTaskViewSet(viewsets.ModelViewSet):
    queryset = UserTask.objects.all()
    serializer_class = UserTaskSerializer
