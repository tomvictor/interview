from rest_framework import serializers
from .models import DataHolder


from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

import json

class CreateSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()
    class Meta:
        model = DataHolder
        fields = ["id", "data"]

    def create(self, validated_data):
        data = validated_data.pop("data")
        _json_data = json.dumps(data)
        instance = DataHolder.objects.create(data=_json_data)
        return instance

class CRUDSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()
    class Meta:
        model = DataHolder
        fields = ["id", "data"]

    def get_data(self,instance):
        try:
            data = json.loads(instance.data)
        except:
            return {}
        return data


class ListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateSerializer


    def list(self, request, *args, **kwargs):
        queryset = DataHolder.objects.all()
        serializer = CRUDSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(CRUDSerializer(instance).data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()



class Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CRUDSerializer
    queryset = DataHolder.objects.all()
