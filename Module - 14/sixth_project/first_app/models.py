from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 23)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    fahter_name = models.TextField(default="rahim")

    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"
