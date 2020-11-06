from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

from core.models import Image
from core.serializers import ImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class IndexView(TemplateView):
    template_name = 'index.html'