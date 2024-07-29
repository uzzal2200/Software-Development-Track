
from django import forms
from .models import CommentsModel,PurchaseModel

class commentFrom(forms.ModelForm):
    class Meta:
        model=CommentsModel
        fields=["name","email","comment"]
