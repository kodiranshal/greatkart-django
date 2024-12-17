from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,  # Passing all available products to the template.  # This is where you can modify the template to display the products in a more meaningful way.  # For example, you can loop over the products in the template and create HTML elements to display each product.  # Also, you can add any other necessary context variables to pass to the template.  # For example, you can pass the total number of products available to the template.  # The template should then be able to access these context variables and display the products and other relevant information.  # If you don't need to modify the template, you can just pass the products variable directly to the render function.  # For example, render(request, 'home.html', {'products': products}) instead of render(request, 'home.html') and then in the template, you can access the products variable using {{ products }}.  # If you need to add more context variables

    }
    return render (request, 'home.html', context)