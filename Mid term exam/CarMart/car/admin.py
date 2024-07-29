
from django.contrib import admin
from .models import CarModel,CommentsModel,PurchaseModel
# Register your models here.
@admin.register(CarModel)
class modelRegister(admin.ModelAdmin):
    prepopulated_fields={"slug":("name","price")}
    list_display=["name","price","quantity","brand","slug"]

@admin.register(CommentsModel)
class CommentRegister(admin.ModelAdmin):
    list_display=["name","email","comment","date"]

@admin.register(PurchaseModel)
class PurshaseRegister(admin.ModelAdmin):
    list_display=["user","car_model","purchase_date"]
