from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import AlbumModel
# Create your views here.
def Album(request):
    if request.method=="POST":
        form=AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_album")
    else:
        form=AlbumForm()
    return render(request,"album/add_album.html",{"form":form})

def AlbumEdit(request,id):
    album=AlbumModel.objects.get(pk=id)
    if request.method=="POST":
          form=AlbumForm(request.POST, instance=album)
          if form.is_valid():
               form.save()
               return redirect("AddHome")
    else:
         form=AlbumForm(instance=album)
    return render(request,"album/add_album.html",{"form":form})

def DeleteAlbum(request,id):
    album=AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect("AddHome")