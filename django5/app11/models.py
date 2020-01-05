from django.db import models

# Create your models here.
class employee(models.Model):
    eid = models.IntegerField()
    name =  models.CharField(max_length=50)
    age = models.IntegerField()