from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import AppSerializer, PublisherSerializer
from api.models import Apps, Publisher
from rest_framework.pagination import PageNumberPagination


class AppsViewSet(ModelViewSet):
    serializer_class = AppSerializer
    queryset = Apps.objects.all()
    pagination_class = PageNumberPagination


class PublisherViewSet(ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    pagination_class = PageNumberPagination
