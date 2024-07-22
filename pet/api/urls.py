from django.urls import path

from .views import BreedViewSet, DogViewSet

urlpatterns = [
    path('dogs/',  DogViewSet.as_view(), name='dog-list'),
    path('dogs/<int:pk>',  DogViewSet.as_view(), name='dog-detail'),
    path('breeds/', BreedViewSet.as_view(), name='breed-list'),
    path('breeds/<int:pk>', BreedViewSet.as_view(), name='Breed-detail')
]
