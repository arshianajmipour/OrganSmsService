from django.shortcuts import render
from django.shortcuts import get_object_or_404
from common_app.serializers import StateSerializer , CitySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from common_app.models import State,City
from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

class StateViewSet(viewsets.ViewSet):


    def list(self, request):
        queryset = State.objects.all()
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = City.objects.filter(state_id=pk)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)



class CityViewSet(viewsets.ViewSet):


    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = City.objects.filter(id=pk)
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)



