from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.conf import settings
from django.utils import timezone

# Create your views here.

class ProfileView(APIView):
  def get(self, request):
    
    data = {
      "email":settings.MY_EMAIL,
      "current_datetime":timezone.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
      "github_url":settings.GITHUB_URL,
    }
    return Response(data, status=status.HTTP_200_OK)