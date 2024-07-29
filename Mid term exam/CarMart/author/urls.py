
from django.urls import path
from . import views
urlpatterns = [
    path("signup/",views.SignUp.as_view(),name="Signup"),
    path("login/",views.Login.as_view(),name="Login"),
    path("profile/",views.Profile.as_view(),name="Profile"),
    path("profile/update/",views.Update,name="Update"),
    path("profile/update/changePassword/",views.ChangePass,name="ChangePass"),
    path("logout/",views.Logout,name="Logout"),
]
