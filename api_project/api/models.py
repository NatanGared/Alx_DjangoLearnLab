from django.db import models

class Id(models.Model):
    fullname = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname