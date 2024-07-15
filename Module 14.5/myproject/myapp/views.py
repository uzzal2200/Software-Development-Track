from django.shortcuts import render, redirect
from .forms import ExtraFieldsForm

# Create your views here.


def extra_fields_view(request):
    if request.method == 'POST':
        form = ExtraFieldsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ExtraFieldsForm()
    return render(request, 'myapp/extra_fields.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html')
