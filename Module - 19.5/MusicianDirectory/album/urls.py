from django.urls import path
from . import views
urlpatterns = [
    path("album/",views.AlbumViewsClass.as_view(),name="add_album"),
    path("edit/<int:id>",views.EditViewsClass.as_view(),name="edit_album"),
]