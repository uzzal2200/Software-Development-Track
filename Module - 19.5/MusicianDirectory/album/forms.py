
from django import forms
from .models import AlbumModel


class AlbumForm(forms.ModelForm):
    class Meta:
        model=AlbumModel
        fields="__all__"
        # exclude=["music"]
        labels={
            "name":"Album Name",
            "rating" : "Rating between 1-5"
        }
