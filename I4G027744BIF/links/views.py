from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Link
from .serializers import LinkSerializers

# Create your views here.

class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializers

class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializers

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializers

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializers

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializers