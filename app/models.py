from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Encoded_Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(blank=True, null=True, max_length=1000)
    creation_date = models.DateTimeField(blank=True, null=True, ) 
