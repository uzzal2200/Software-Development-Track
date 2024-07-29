from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from album.models import AlbumModel
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class RegisterViewsClass(CreateView):
    form_class=forms.RegistationForm
    template_name="registationFrom.html"
    success_url=reverse_lazy("LogIn_page")

class LoginViewsClass(LoginView):
    template_name="loginForm.html"
    success_url=reverse_lazy("profile_page")

@method_decorator(login_required,name="dispatch")
class ProfileViewClass(TemplateView):
    template_name="profilePage.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=AlbumModel.objects.all()
        return context
