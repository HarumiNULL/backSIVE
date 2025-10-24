from rest_framework import serializers
from api.models import Product

class ProductSerializers(serializers.ModelSerializer): 
    class Meta:
        model = Product
        fields =['id_product','nameProduct']
        read_only_fields = ['id_product','nameProduct']
    