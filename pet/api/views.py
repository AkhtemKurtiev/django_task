from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class DogViewSet(APIView):

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            dog = get_object_or_404(Dog, pk=pk)
            serializer = DogSerializer(dog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            dogs = Dog.objects.all()
            serializer = DogSerializer(dogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk,  *args, **kwargs):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, redquest, pk, *args, **kwargs):
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedViewSet(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            breed = get_object_or_404(Breed, pk=pk)
            serializer = BreedSerializer(breed)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            breed = Breed.objects.all()
            serializer = BreedSerializer(breed, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.datam, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        breed = get_object_or_404(Breed, pk=pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
