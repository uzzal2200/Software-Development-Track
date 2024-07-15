from django.urls import path
from . import views
urlpatterns = [
    path("album/",views.Album,name="add_album"),
    path("edit/<int:id>",views.AlbumEdit,name="edit_album"),
    path("delete/<int:id>",views.DeleteAlbum,name="delete_album"),
]