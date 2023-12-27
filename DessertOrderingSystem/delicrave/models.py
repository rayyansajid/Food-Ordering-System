from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(db_column = "UserName",
                                max_lenth = 10,
                                null = False,
                                blank = False)                                
    password = models.CharField(db_column = "Password",
                                max_lenth = 10,
                                min_length = 6,
                                null = False,
                                blank = False)
    name =  models.CharField(db_column = "Name",
                             max_lenth = 20,
                            null = False,
                            blank = False)
    contact = models.PhoneNumberField(db_column = "contact",
                                      unique = 1,
                                      null = False,
                                      blank = False)
    email = models.EmailField(db_column = "Email",
                              null = False,
                              blank = False)
    address = models.CharField(db_column = "Address",
                               null = False,
                               blank = False,
                               max_length = 50)
    
class Category(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            blank = False,
                            max_length = 10)
    
    
class Flavor(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            blank = False,
                            max_length = 10)
    
class Feedback(models.Model):
    rating = models. IntegerField(db_column = "Rating",
                                  blank = True,
                                  null = True)
    review = models.CharField(db_column = "Review",
                            null = True,
                            blank = False,
                            max_length = 100)
    #Order
    #Desert

class Desert(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            blank = False,
                            max_length = 10)
    stockquantity = models. IntegerField(db_column = "Stock Quantity",
                                  blank = True,
                                  null = True)
    description = models.CharField(db_column = "Description",
                            null = True,
                            max_length = 100)
    #Desert_cat relation
    category = models.ForeignKey(Category,
                                 db_column = 'Category',
                                 on_delete = models.CASCADE,blank=True,
                                 null=True)
class Unit(models.Model):
    unitname = models.CharField(db_column = "Name",
                            null = False,
                            max_length = 10,blank=True,
                            null=True)


class Order(models.Model):
    date = models.DateField(auto_now=True)
    status = models.CharField(choices = (
                                        ('Pending','Pending'),
                                        ('Confirmed','Confirmed'),
                                        ('On The Way','On The Way'),
                                        ('Delivered','Delivered')
                                    ),
                                    blank=True,
                                    null=True)
    totalamount = models.FloatField(blank=True,
                                    null=True)
    paymethod = models.CharField(choices = (
                                        ('COD','COD'),
                                        ('CARD','CARD')
                                    ),
                                    blank=True,
                                    null=True)
    
#RelationShips:
#cat_flavour
class FlavorCat(models.Model):
    Flavor = models.ManyToManyField(Flavor,
                                    db_column = "Flavor",blank=True,
                                    null=True)
    Category = models.ManyToManyField(Category,
                                      db_column = "Category",blank=True,
                                      null=True)

class Wishlist(models.Model):
    Customer = models.ManyToManyField(Customer,
                                      db_column = "Customer",blank=True,
                                      null=True)
    Desert = models.ManyToManyField(Desert,
                                    db_column = "Desert",blank=True,
                                    null=True) 
#UnitPrice
class CatalogItem(models.Model):
    Desert = models.ManyToManyField(Desert,
                                    db_column = "Desert",blank=True,
                                    null=True)
    Unit = models.ManyToManyField(Unit,
                                  db_column="Unit",blank=True,
                                  null=True)
    Price = models.FloatField(default = 0.0,
                              null=True,
                              blank = True,blank=True,
                              null=True)
# since single customer will have only one cart, there is 
# no need to insert a layer by making a cart table. We can just add 
# customer to cartItems
class CustomerCart(models.Model):
    customer = models.ManyToManyField(Customer,
                                      db_column = 'Customer',blank=True,
                                      null=True)


# New relation between CatalogueItem and Cart:    
# ~ Many CatalogItems can map to single Cart
# ~ Many Carts can map to single CatalogItem
# ~ Quantity of that CatalogItem.
class CartItem(models.Model):
    catalogitem = models.ManyToManyField(CatalogItem,
                                         db_column = 'CatalogItem',blank=True,
                                         null=True)
    cart = models.ForeignKey(CustomerCart,
                             db_column = 'CustomerCart',blank=True,
                             null=True)
    quantity = models.IntegerField(blank=True,
    null=True)
