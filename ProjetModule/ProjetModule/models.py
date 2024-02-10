from django.contrib.auth.models import User
from django.db import models


class Session(models.Model):
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    is_open = models.BooleanField(default=False)

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    progress_percentage = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    understanding = models.CharField(max_length=20)