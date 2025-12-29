from django.db import models
from django.contrib.auth.models import User
from companies.models import Company

class Application(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.company.name}"
