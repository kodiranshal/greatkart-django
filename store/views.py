from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,  # Passing all available products to the template.  # This is where you can modify the template to display the products in a more meaningful way.  # For example, you can loop over the products in the template and create HTML elements to display each product.  # Also, you can add any other necessary context variables to pass to the template.  # For example, you can pass the total number of products available to the template.  # The template should then be able to access these context variables and display the products and other relevant information.  # If you don't need to modify the template, you can just pass the products variable directly to the render function.  # For example, render(request, 'home.html', {'products': products}) instead of render(request, 'home.html') and then in the template, you can access the products variable using {{ products }}.  # If you need to add more context variables
        'product_count': product_count,
    }
    return render (request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e 
    
    context = {
        'single_product': single_product,
    }
    
    return render(request, 'store/product_detail.html', context)