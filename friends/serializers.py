from rest_framework import serializers
from .models import Countries, Cities, Friends


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('id', 'name')


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id', 'name', 'country')


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = (
            'id', 'name', 'dob', 'facebook', 'instagram', 'phone_number', 'email', 'address', 'postal_code', 'city', 'created_at', 'modified_at')
