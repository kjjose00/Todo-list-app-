from atexit import register
from django.contrib import admin
from .models import CustomUser,Todos
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','email']

@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display=['user','text']