from django.db import models

class ExtraFieldsModel(models.Model):
    char_field = models.CharField(max_length=100)
    integer_field = models.IntegerField()
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    email_field = models.EmailField()
    boolean_field = models.BooleanField()
    text_field = models.TextField()

    def __str__(self):
        return self.char_field
