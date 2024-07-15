from django.urls import path
from .views import extra_fields_view, success_view

urlpatterns = [
    path('form/', extra_fields_view, name='extra_fields'),
    path('success/', success_view, name='success'),
]
