from rest_framework import serializers
from api.models import User

class UsersSerializers(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields =['id','first_name','last_name','email','role','state']
        read_only_fields =['id']
    