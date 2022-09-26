from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True, blank=True)
    title =
    description =
    complete =
    create =
