from django.shortcuts import render
from rest_framework import generics
from apis.models import (Incident, Organization, Individual)
from.serializers import (IncidentSerializer,
                         OrganizationSerializer,
                         IndividualSerializer)

from rest_framework import viewsets
from rest_framework.response import Response

from apis import serializers
from apis import models

from rest_framework import status



class HelloViewSet(viewsets.ViewSet):
    """Test API View"""
    serializer_class = serializers.IncidentSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'automatically maps to URLS using routers',
            'provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(selfs, request, pk=None):
        """Handle updating an Object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial updates on object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an Object"""
        return Response({'http_method': 'DELETE'})