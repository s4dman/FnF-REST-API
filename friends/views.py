from django.shortcuts import render
from rest_framework import viewsets
from .models import Friends
from .serializers import FriendSerializer


# Create your views here.
class FriendsView(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendSerializer
