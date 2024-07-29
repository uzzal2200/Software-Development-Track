from django.shortcuts import render
from album.models import AlbumModel
from django.views.generic import TemplateView

class HomeViewClass(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=AlbumModel.objects.all()
        return context