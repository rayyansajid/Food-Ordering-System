from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(db_column = "UserName",
                                max_length = 15,
                                null = False,
                                blank = False)                                
    password = models.CharField(db_column = "Password",
                                max_length = 15,
                                null = False,
                                blank = False)
    name =  models.CharField(db_column = "Name",
                             max_length = 30,
                            null = False,
                            blank = False)
    contact = models.CharField(db_column = "contact",
                               max_length = 15,
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
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            blank = False,
                            max_length = 20)
    image = models.ImageField(upload_to='category_images/', 
                              null=True, 
                              blank=True)
    def __str__(self):
        return self.name
    
class Flavor(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            blank = False,
                            max_length = 20)
    def __str__(self):
        return self.name
    
class Dessert(models.Model):
    name = models.CharField(db_column = "Name",
                            null = False,
                            blank = False,
                            max_length = 20)
    stockquantity = models. IntegerField(db_column = "Stock Quantity",
                                  blank = True,
                                  null = True)
    description = models.CharField(db_column = "Description",
                            null = True,
                            max_length = 100)
    unit = models.CharField(null = True,
                            blank = True, 
                            db_column="Unit",
                            max_length = 25)
    price = models.FloatField(default = 0.0,
                              null = False,
                              blank = False)
    image = models.ImageField(upload_to='dessert_images/', 
                              null=True, 
                              blank=True)
    #Dessert_cat relation
    category = models.ForeignKey(Category,
                                 db_column = 'Category',
                                 on_delete = models.CASCADE,blank=True,
                                 null=True)
    flavor = models.ForeignKey(Flavor,
                               db_column = 'Flavor',
                               on_delete = models.CASCADE,
                               null=True,
                               blank = False)
    def __str__(self):
        return self.name
class Order(models.Model):
    choices = (
                ('Pending','Pending'),
                ('Confirmed','Confirmed'),
                ('On The Way','On The Way'),
                ('Delivered','Delivered'),
                ('Cancel','Cancel')
            )
    paychoices = (
                ('COD','COD'),
                ('CARD','CARD')
            )
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length = 10,
                              choices = choices,
                              blank=True,
                              null=True,
                              default = "Pending")
    totalamount = models.FloatField(blank=True,
                                    null=True)
    paymethod = models.CharField(max_length = 10,
                                 choices = paychoices,
                                 blank=True,
                                 null=True)
    rating = models. IntegerField(db_column = "Rating",
                                  blank = True,
                                  null = True)
    review = models.CharField(db_column = "Review",
                            null = True,
                            blank = True,
                            max_length = 100)
    customer = models.ForeignKey(Customer,
                                 db_column = 'customer_id',
                                 blank=False,
                                 null=False,
                                 on_delete = models.CASCADE)
    def __str__(self):
        return f"Order#{self.id}: {self.customer.name}\'s"
    

#RelationShips:

#cat_flavour
    #
class FlavorCat(models.Model):
    flavor = models.ForeignKey(Flavor,
                               on_delete = models.CASCADE,
                               null = True,
                               blank = True, 
                               db_column = "Flavor")
    category = models.ForeignKey(Category,
                               on_delete = models.CASCADE,
                               null = True,
                               blank = True, 
                               db_column = "Category")
    def __str__(self):
        return f"{self.category.first()}: {self.flavor.first()}"

class Wishlist(models.Model):
    customer = models.OneToOneField(Customer,
                                   on_delete = models.CASCADE,
                                   null = True,
                                   blank = True, 
                                   db_column = "Customer")
    dessert = models.ManyToManyField(Dessert,
                                    db_column = "Dessert")
    def __str__(self):
        return f"WishList for Cust#{self.customer.id}"
    
#UnitPrice

class CustomerCart(models.Model):
    customer = models.OneToOneField(Customer, 
                                    on_delete = models.CASCADE,
                                    db_column = 'Customer')
    def __str__(self):
        return f"{self.customer}'s Cart"
    
# New relation between CatalogueItem and Cart:    
# ~ Many desserts can map to single Cart
# ~ Many Carts can map to single dessert
# ~ Quantity of that dessert.
class CartItem(models.Model):
    dessert = models.ForeignKey(Dessert,
                                    on_delete = models.CASCADE,
                                    null = True,
                                    blank = True, 
                                    db_column = 'Dessert')
    cart = models.ForeignKey(CustomerCart,
                                db_column = 'CustomerCart',
                                blank=True,
                                null=True,
                                on_delete = models.CASCADE)
    quantity = models.IntegerField(blank=True,
                                   null=True)
    def __str__(self):
        return f"Cart#{self.cart.id}: {self.dessert}"
    
class OrderItem(models.Model):
    dessert = models.ForeignKey(Dessert,
                                    on_delete = models.CASCADE,
                                    null = True,
                                    blank = True,
                                    db_column = 'dessert')
    order = models.ForeignKey(Order,
                             db_column = 'Order',
                             blank=False,
                             null=False,
                             on_delete = models.CASCADE)
    quantity = models.IntegerField(blank=True,
                                   null=True)
    def __str__(self):
        return f"Order#{self.order.id}"