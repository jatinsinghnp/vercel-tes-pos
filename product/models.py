from django.db import models


from root.utils import BaseModel
from user.models import Customer


class ProductCategory(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Category Title")
    slug = models.SlugField(unique=True, verbose_name="Category Slug")
    description = models.TextField(
        verbose_name="Category Description", null=True, blank=True
    )

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Product Name")
    slug = models.SlugField(unique=True, verbose_name="Product Slug")
    description = models.TextField(
        null=True, blank=True, verbose_name="Product Description"
    )
    unit = models.CharField(null=True, max_length=50, blank=True)
    is_taxable = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="product/images/", null=True, blank=True)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    product_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - Rs. {self.price} per {self.unit}"


from django.contrib.auth import get_user_model

User = get_user_model()


class CustomerProduct(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    price = models.FloatField(default=0.0)
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.product.title} - Rs. {self.price}"
