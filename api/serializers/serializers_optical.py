from api.models import Optical
from rest_framework import serializers

class OpticalSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Optical
        fields = '__all__'