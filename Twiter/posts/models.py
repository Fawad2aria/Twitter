from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chirps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chirps')
    message = models.CharField(max_length=128)
    created_at = models.DateTimeField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    
