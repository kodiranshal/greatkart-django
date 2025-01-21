from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,  # Passing all available products to the template.  # This is where you can modify the template to display the products in a more meaningful way.  # For example, you can loop over the products in the template and create HTML elements to display each product.  # Also, you can add any other necessary context variables to pass to the template.  # For example, you can pass the total number of products available to the template.  # The template should then be able to access these context variables and display the products and other relevant information.  # If you don't need to modify the template, you can just pass the products variable directly to the render function.  # For example, render(request, 'home.html', {'products': products}) instead of render(request, 'home.html') and then in the template, you can access the products variable using {{ products }}.  # If you need to add more context variables
        'product_count': product_count,
    }
    return render (request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
       
    except Exception as e:
        raise e 
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,  # This variable is used to determine if the current product is already in the user's shopping cart.  # If the product is in the cart, the variable will be True.  # If the product is not in the cart, the variable will be False.  # This variable is then used in the template to display a different message or button for the user to add the product to their cart.  # You can modify the template to
    }
    
    return render(request, 'store/product_detail.html', context)

def search (request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products' : products,
        'product_count' : product_count,
    }
    
    return render (request, 'store/store.html', context)
    # return HttpResponse("Search results")