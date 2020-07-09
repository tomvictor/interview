from django.db import models

# Create your models here.


class DataHolder(models.Model):
    data = models.TextField(null=True)

    def __str__(self):
        return str(self.id)
