from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    package = models.CharField(max_length=50)

    def __str__(self):
        return self.name


