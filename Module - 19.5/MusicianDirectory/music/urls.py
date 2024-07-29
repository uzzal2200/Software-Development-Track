
from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.MusicViewsClass.as_view(),name="addMusic"),
    path("music_edit/<int:id>",views.EditMusicViewClass.as_view(),name="musicEdit"),
    path("delete/<int:id>",views.DeleteViewsClass.as_view(),name="delete_album"),
]
