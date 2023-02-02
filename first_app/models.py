from django.db import models

# Create your models here.
class Comp(models.Model):
    name = models.CharField(max_length=100,null=True)
    bank_name = models.CharField(max_length=199,null=False)
    branch = models.CharField(max_length=50,blank=True)