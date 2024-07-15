from django import forms
from .models import ExtraFieldsModel

class ExtraFieldsForm(forms.ModelForm):
    char_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    integer_field = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date_field = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    datetime_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    email_field = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    url_field = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    boolean_field = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    text_field = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = ExtraFieldsModel
        fields = '__all__'
