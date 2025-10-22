from api.models import User
from rest_framework import serializers, viewsets
from api.serializers import UsersSerializers
from permissions import IsAdminUser

class UsersController(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UsersSerializers
    permission_classes= [IsAdminUser]
    
    http_method_names =['get','post','delete']