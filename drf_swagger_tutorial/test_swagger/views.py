from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf_swagger_tutorial.test_swagger.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
