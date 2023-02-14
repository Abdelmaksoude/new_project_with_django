from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
import datetime
from django_countries.fields import CountryField
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , verbose_name=("User") , on_delete=models.CASCADE)
    slug = models.SlugField(blank=True , null=True)
    address = models.CharField(max_length=100)
    country = CountryField()
    image = models.ImageField(upload_to='profile_img' , verbose_name=("image") , null=True , blank=True)
    join_date = models.DateTimeField(verbose_name=("join date") , default=datetime.datetime.now)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('accounts:Profile_details' , kwargs={'slug':self.slug})

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile , self).save(*args , **kwargs)

def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile , sender=User)