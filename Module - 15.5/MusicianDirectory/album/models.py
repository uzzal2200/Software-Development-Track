from django.db import models
from music.models import MusicModel
# Create your models here.
Rating = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
]
class AlbumModel(models.Model):
    name=models.CharField(max_length=40)
    music=models.ForeignKey(MusicModel, on_delete=models.CASCADE)
    release_date=models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=Rating)
    
    def __str__(self):
        return self.name