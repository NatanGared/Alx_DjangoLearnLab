from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_by = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname