from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225, blank=False, null=False)
    content = models.TextField(max_length=1000, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now())