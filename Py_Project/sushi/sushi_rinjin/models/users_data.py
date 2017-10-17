from django.db import models


class UsersData(models.Model):
    user_name = models.CharField(max_length=50)
    tel = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
