from django.db import models

class Userlog(models.Model):
    name=models.CharField(max_length=500)
    comments=models.CharField(max_length=500)

