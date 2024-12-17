from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

#link ke deskripsi
    def get_url (self):
        return reverse('product_detail', args=[self.category.slug, self.slug])  # Assuming 'product_detail' is the name of your product detail view and 'category.slug' and'self.slug' are the slugs of the category and the product, respectively.  # If your view name is different or the slugs are different, you will need to adjust this line accordingly.  # This will return the URL to the product detail page.  # You can then use this URL in your template to link to the product detail page.  # For example, in your template, you can use: <a href="{{ product.get_url }}">View Product</a>.  # This will link to the product detail page for the given product.  # If you want to link to the product detail page for all products in a given category, you can use: <a href="{{ category.get_url }}">View All Products</a

    def __str__(self):
        return self.product_name

