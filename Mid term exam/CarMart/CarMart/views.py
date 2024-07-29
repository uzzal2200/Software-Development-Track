
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from category.models import CategoryModel
from car.models import CarModel,PurchaseModel
from car.forms import commentFrom
from django.views.generic.detail import DetailView
# Create your views here.

def Home(request,category_slug=None):
    categorys=CategoryModel.objects.all()
    cars=CarModel.objects.all()
    if category_slug is not None:
        category=CategoryModel.objects.get(slug=category_slug)
        cars=CarModel.objects.filter(brand=category)
    return render(request,"home.html",{"category":categorys,"Brand":cars})

class DetailsCar(DetailView):
    model=CarModel
    template_name="carDetails.html"
    def post(self,request,*args,**kwargs):
        comment_form=commentFrom(data=self.request.POST)
        car_object=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.carComment=car_object
            new_comment.save()
        if "buy_car" in request.POST:
            if car_object.quantity > 0:
                car_object.quantity -=1
                car_object.save()
                PurchaseModel.objects.create(user=request.user, car_model=car_object)
                messages.success(request, 'Car purchased successfully!')
            else:
                messages.warning(self.request, 'All Car is Sold out please look forward')
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        comment_post=self.get_object()
        context["carDetail"]=CarModel.objects.filter(slug=self.kwargs.get("slug"))
        context["CarBrand"]=CarModel.objects.get(slug=self.kwargs.get("slug"))
        context["comments"]=comment_post.comments.all()
        context["commentForm"]=commentFrom()
        return context
