from django.db import models

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=20,primary_key=True)
    mobile = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return "-".join([self.name, self.address])