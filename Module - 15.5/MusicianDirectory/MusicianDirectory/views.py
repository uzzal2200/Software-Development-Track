from django.shortcuts import render
from album.models import AlbumModel
def Home(request):
    album=AlbumModel.objects.all()
    return render(request,"home.html",{"data":album})