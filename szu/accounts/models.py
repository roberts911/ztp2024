# filepath: /home/rsiurek/szu/accounts/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nip = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    api_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.name