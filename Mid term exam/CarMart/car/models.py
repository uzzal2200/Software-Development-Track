
from django.db import models
from django.contrib.auth.models import User
from category.models import CategoryModel
# Create your models here.
class CarModel(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    discription=models.TextField()
    brand=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="car/media/uploads/", blank=True, null=True)
    slug=models.SlugField(max_length=100, unique=True ,blank= True,null=True)

    def __str__(self):
        return self.slug

class CommentsModel(models.Model):
    carComment=models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=100)
    email=models.EmailField()
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class PurchaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="userName")
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
