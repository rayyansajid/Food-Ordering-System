from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(db_column = "UserName",
                                max_lenth = 10,
                                null = False)                                
    password = models.CharField(db_column = "Password",
                                max_lenth = 10,
                                min_length = 6,
                                null = False)
    name =  models.CharField(db_column = "Name",
                             max_lenth = 20,
                             null = False)
    contact = models.PhoneNumberField(db_column = "contact",
                                      unique = 1,
                                      null = False)
    email = models.EmailField(db_column = "Email",
                              null = False)
    address = models.CharField(db_column = "Address",
                               null = False,
                               max_length = 50)
    
class Category(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            max_length = 10)
    
    
class Flavor(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            max_length = 10)
    
class Feedback(models.Model):
    rating = models. IntegerField(db_column = "Rating",
                                  blank = True,
                                  null = True)
    review = models.CharField(db_column = "Review",
                            null = True,
                            max_length = 100)
    #Order
    #Desert

class Desert(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            max_length = 10)
    stockquantity = models. IntegerField(db_column = "Stock Quantity",
                                  blank = True,
                                  null = True)
    description = models.CharField(db_column = "Description",
                            null = True,
                            max_length = 100)
    #category
    #unit

class FlavorCat(models.Model):
    Flavor = models.ManyToManyField(Flavor,
                                    db_column = "Flavor")
    Category = models.ManyToManyField(Category,
                                      db_column = "Category")

# class Cart(models.Model):
#     CatalogItems = models.

class Wishlist(models.Model):
    Customer = models.ManyToManyField(Customer,
                                      db_column = "Customer")
    Desert = models.ManyToManyField(Desert,
                                    db_column = "Desert")
    
class Unit(models.Model):
    unitname = models.CharField(db_column = "Name",
                            null = False,
                            max_length = 10)
    
class Catalog(models.Model):
    Desert = models.ManyToManyField(Desert,
                                    db_column = "Desert")
    Unit = models.ManyToManyField(Unit,
                                  db_column="Unit")
    Price = models.FloatField(default = 0.0,
                              null=True,
                              blank = True)
    