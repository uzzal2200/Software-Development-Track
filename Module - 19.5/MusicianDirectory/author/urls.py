
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("registation/",views.RegisterViewsClass.as_view(),name="registations_page"),
    path("login/",views.LoginViewsClass.as_view(),name="LogIn_page"),
    path("profile/",views.ProfileViewClass.as_view(),name="profile_page"),
    path("logout/",LogoutView.as_view(),name="Logout_page"),
]
