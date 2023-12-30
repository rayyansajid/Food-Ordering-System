from django.contrib import admin
from delicrave.models import *
# Register your models here.


admin.site.register(Customer)

admin.site.register(Dessert)
# class DessertAdmin(admin.ModelAdmin):
    # list_display  = [field.name for field in Dessert._meta.get_fields()]
    
    
admin.site.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
    # list_display  = [field.name for field in Category._meta.get_fields()]

admin.site.register(Flavor)
# class FlavorAdmin(admin.ModelAdmin):
#     list_display  = [field.name for field in Flavor._meta.get_fields()]
    

# admin.site.register(Feedback)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display  = [field.name for field in Feedback._meta.get_fields()]
    
admin.site.register(Unit)
# class UnitAdmin(admin.ModelAdmin):
#     list_display  = [field.name for field in Unit._meta.get_fields()]
    
admin.site.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display  = [field.name for field in Order._meta.get_fields()]
    
admin.site.register(FlavorCat)
        
admin.site.register(Wishlist)
            
admin.site.register(CatalogItem)

admin.site.register(CustomerCart)

admin.site.register(CartItem)


admin.site.register(OrderItem)
