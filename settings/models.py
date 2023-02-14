from django.db import models

# Create your models here.
class Brand(models.Model):
    BRAname = models.CharField(max_length=50)
    BRAdesc = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.BRAname

class Variant(models.Model):
    VARname = models.CharField(max_length=50)
    VARdesc = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.VARname