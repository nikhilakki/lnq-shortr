from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    long_url = models.TextField()
    short_url = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.long_url
    