from django.shortcuts import render , get_object_or_404
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    context = {'product_list': product_list}
    return render(request , 'Product/product_list.html' , context)

def product_details(request , slug):
    # product_details = Product.objects.get(Proslug=slug)
    product_details = get_object_or_404(Product , Proslug=slug)
    context = {'product_details': product_details}
    return render(request , 'Product/product_details.html' , context)
