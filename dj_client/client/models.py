from django.db import models


class UserData(models.Model):
    user_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    authorization_code = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    expires_in = models.PositiveSmallIntegerField()
    token_type = models.CharField(max_length=25)
    info = models.CharField(max_length=100)
