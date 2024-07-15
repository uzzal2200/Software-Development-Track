from django.shortcuts import render,redirect
from .forms import MusicForm
from .models import MusicModel
# Create your views here.
def Music(request):
    if request.method=="POST":
        form=MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addMusic")
        
    else:
        form=MusicForm()
    return render(request,"music/add_music.html",{"form":form})

def MusicEdit(request,id):
    music=MusicModel.objects.get(pk=id)
    if request.method=="POST":
          form=MusicForm(request.POST, instance=music)
          if form.is_valid():
               form.save()
               return redirect("AddHome")
    else:
         form=MusicForm(instance=music)
    return render(request,"music/add_music.html",{"form":form})
          