from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(null=True)
    price = models.IntegerField(null=True)
    offer = models.BooleanField(default=False)