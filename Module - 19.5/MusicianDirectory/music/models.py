from django.db import models

# Create your models here.
class MusicModel(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    Email=models.EmailField(unique=True)
    Phone_Number=models.CharField(max_length=15)
    Intrument=models.CharField(max_length=50)

    def __str__(self):
        return self.First_Name