from django.db import models


class Friends(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
