from django.contrib import admin
from delicrave.models import *
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username','password', 'name', 'contact', 'email','address']

@admin.register(Desert)
class desertAdmin(admin.ModelAdmin):
    list_display  = [field.name for field in Desert._meta.get_fields()]
    
    
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display  = [field.name for field in Category._meta.get_fields()]

@admin.register(Flavor)
class flavorAdmin(admin.ModelAdmin):
    list_display  = [field.name for field in Flavor._meta.get_fields()]
    

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display  = [field.name for field in Feedback._meta.get_fields()]
    
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display  = [field.name for field in Unit._meta.get_fields()]