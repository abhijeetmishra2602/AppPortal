from rest_framework import viewsets, permissions
from .models import UserProfile, Task
from .serializers import UserProfileSerializer, TaskSerializer
from django.shortcuts import render

def user_interface(request):
    # Fetch data from your API
    api_url = 'http://127.0.0.1:8000/api/user/android-apps/'
    response = requests.get(api_url)

    if response.status_code == 200:
        apps = response.json()  # Assuming the API returns a JSON list of apps
    else:
        apps = []

    return render(request, 'user_portal/user_interface.html', {'apps': apps})

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
