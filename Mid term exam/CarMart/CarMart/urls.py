"""
URL configuration for CarMart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home, name="Home"),
    path("category/<slug:category_slug>",views.Home, name="FilterCategory"),
    path("accounts/",include("author.urls")),
    path("Details/<slug:slug>/",views.DetailsCar.as_view(), name="carDetails"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
