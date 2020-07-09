from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import DataHolder


from rest_framework import generics
from rest_framework.permissions import AllowAny


class CRUDSerializer(serializers.Serializer):
    class Meta:
        model = DataHolder
        fields = "__all__"


class Create(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializers = CRUDSerializer


class List(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializers = CRUDSerializer
