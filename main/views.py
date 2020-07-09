from rest_framework import serializers
from .models import DataHolder


from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response


class CRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataHolder
        fields = ["id", "data"]


class ListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CRUDSerializer
    queryset = DataHolder.objects.all()


class Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CRUDSerializer
    queryset = DataHolder.objects.all()
