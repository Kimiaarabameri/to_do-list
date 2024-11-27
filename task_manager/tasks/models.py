from django.db import models
from accounts.models import Account
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title