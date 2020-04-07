from rest_framework import viewsets, permissions
from .models import Countries, Cities, Friends
from .serializers import CountriesSerializer, CitiesSerializer, FriendSerializer


class CountriesView(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    # Model-level permission, only authenticated users can access this view
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CitiesView(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class FriendsView(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendSerializer
