from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
# Create your views here.

from users.serializers import UserSerializer

@api_view(['GET'])
@permission_required([IsAuthenticated])
def user_view(recuest):
    seriazlizer=UserSerializer(recuest.user)
    return Response(seriazlizer.data)