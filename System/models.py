from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    balance = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user_id
