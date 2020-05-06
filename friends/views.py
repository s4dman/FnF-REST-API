from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = FriendSerializer(queryset)
        return Response(serializer.data)

    def post(self, request):
        serializer = FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk=id)
        serializer = FriendSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)
