from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    ProName = models.CharField(max_length=50 , verbose_name=("Name"))
    Procategory = models.ForeignKey('category' , on_delete=models.CASCADE , null=True , blank= True , verbose_name=("Category"))
    Probrand = models.ForeignKey('settings.Brand' , on_delete=models.CASCADE , null=True , blank= True , verbose_name=("Brand"))
    ProDesc = models.TextField(verbose_name=("Description"))
    Proimage = models.ImageField(upload_to='product/' , verbose_name='image' , null=True , blank=True)
    ProPrice = models.DecimalField(max_digits=6 , decimal_places=2 , verbose_name=("Price"))
    ProDiscountPrice = models.DecimalField(max_digits=6 , decimal_places=2 , verbose_name=("Discount Price"))
    ProCost = models.DecimalField(max_digits=6 , decimal_places=2 , verbose_name=("Cost"))
    ProCreated = models.DateTimeField(verbose_name=("Created In"))
    Proslug = models.SlugField(null=True , blank=True , verbose_name=("Product Slug"))
    Proisnew = models.BooleanField(default=True , verbose_name=("Is New"))
    Proisbestsaller = models.BooleanField(default=False , verbose_name=("Is The BestSaller"))

    def __str__(self):
        return self.ProName

    def save(self , *args , **kwargs):
        if not self.Proslug:
            self.Proslug = slugify(self.ProName)
        super(Product , self).save(*args , **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_details' , kwargs={'slug':self.Proslug})

class ProductImage(models.Model):
    PROIproduct = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name=("Product"))
    PROIimage = models.ImageField(upload_to='product/' , verbose_name=("Image"))

    def __str__(self):
        return str(self.PROIproduct)

class Category(models.Model):
    CATmain_category = models.CharField(max_length=50  , verbose_name=("Main Category"))
    CATparent = models.ForeignKey('self' , limit_choices_to={'CATparent__isnull':True} , on_delete=models.CASCADE , null=True , blank=True , verbose_name=("The Parent"))
    CATdes = models.TextField(verbose_name=("Description"))
    CATimg = models.ImageField(upload_to='category/' , verbose_name=("Image"))

    def __str__(self):
        return str(self.CATmain_category)

class ProductAlternative(models.Model):
    PALNproduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='Main_Product' , verbose_name=("Product"))
    PALNalternative = models.ManyToManyField(Product , related_name='Alternative_Product' , verbose_name=("Product Alternative"))

    def __str__(self):
        return str(self.PALNproduct)

class ProductAcsessories(models.Model):
    PACCproduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='Product_Name' , verbose_name=("Product"))
    PACCalternative = models.ManyToManyField(Product , related_name='Acessoires' , verbose_name=("Product Alternative"))

    def __str__(self):
        return str(self.PACCproduct)