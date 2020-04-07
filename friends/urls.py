from django.urls import path, include
from .views import CountriesView, CitiesView, FriendsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('countries', CountriesView)
router.register('cities', CitiesView)
router.register('friends', FriendsView)

urlpatterns = [
    path('', include(router.urls))
]
