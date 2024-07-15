from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.Music,name="addMusic"),
    path("music_edit/<int:id>",views.MusicEdit,name="musicEdit"),
]

