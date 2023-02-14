from django.contrib import admin
from .models import Product , ProductImage , Category , ProductAlternative , ProductAcsessories
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductAlternative)
admin.site.register(ProductAcsessories)