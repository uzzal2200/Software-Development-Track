
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm 
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib import messages
from car.models import PurchaseModel
from django.contrib.auth import logout,update_session_auth_hash
# Create your views here.

class SignUp(CreateView):
    form_class=forms.SignUpForm
    template_name='author/signup.html'
    success_url=reverse_lazy("Login")

class Login(LoginView):
    template_name="author/login.html"
    success_url=reverse_lazy("Profile")
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form: AuthenticationForm):
        messages.warning(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)

@method_decorator(login_required,name="dispatch")
class Profile(ListView):
    model=PurchaseModel
    template_name="author/profile.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["purchased"]=PurchaseModel.objects.filter(user=self.request.user)
        return context
    
@login_required
def Update(request):
    if request.method=="POST":
        update_form=forms.ChangeInfo(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Successfully Updated!")
            return redirect("Update")
    else:
        update_form=forms.ChangeInfo(instance=request.user)
    return render(request, "author/update.html",{"form":update_form})

@login_required
def ChangePass(request):
    if request.method=="POST":
        changePass_form=PasswordChangeForm(request.user ,data=request.POST)
        if changePass_form.is_valid():
            changePass_form.save()
            messages.success(request, "Successfully Changed!")
            update_session_auth_hash(request,request.user)
            return redirect("Update")
    else:
        changePass_form=PasswordChangeForm(request.user)
    return render(request, "author/passChange.html",{"form":changePass_form})

@login_required
def Logout(request):
    logout(request)
    return redirect("Login")
