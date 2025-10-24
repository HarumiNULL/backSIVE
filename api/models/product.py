from django.db import models

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    nameProduct= models.CharField(max_length=100)
    
    class Meta: 
        managed= True
        db_table= 'product'