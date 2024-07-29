from django.shortcuts import render,redirect
from .forms import MusicForm
from .models import MusicModel
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required,name="dispatch")
class MusicViewsClass(CreateView):
    form_class=MusicForm
    template_name="Music/add_music.html"
    success_url=reverse_lazy("add_album")

@method_decorator(login_required,name="dispatch")
class EditMusicViewClass(UpdateView):
    model=MusicModel
    form_class=MusicForm
    template_name="Music/add_music.html"
    success_url=reverse_lazy("AddHome")
    pk_url_kwarg="id"

@method_decorator(login_required,name="dispatch")
class DeleteViewsClass(DeleteView):
    model=MusicModel
    template_name="Music/confirm_delete.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("profile_page")
