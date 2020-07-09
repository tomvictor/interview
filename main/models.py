from django.db import models

# Create your models here.


class DataHolder(models.Model):
    data = models.TextField(null=True)
