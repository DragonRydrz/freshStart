from django.db import models
from uuid import uuid4
# Create your models here.
from django.contrib.auth.models import User

BOOL_CHOICE = (('True', 'True'), ('False', 'False'))


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30)
    address = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PrivateBookmark(Bookmark):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
