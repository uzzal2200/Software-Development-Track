from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import AlbumModel
from django.views.generic.edit import UpdateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required,name="dispatch")
class AlbumViewsClass(CreateView):
    form_class=AlbumForm
    template_name="album/add_album.html"
    success_url=reverse_lazy("AddHome")

@method_decorator(login_required,name="dispatch")
class EditViewsClass(UpdateView):
    model=AlbumModel
    form_class=AlbumForm
    template_name="album/add_album.html"
    success_url=reverse_lazy("profile_page")
    pk_url_kwarg="id"
