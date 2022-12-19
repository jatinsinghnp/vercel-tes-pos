from django.db import models

# Create your models here.
class DiscountTabe(models.Model):
    class DiscountType(models.TextChoices):
        PERCENTAGE = ("PCT",)
        FLAT = "FLAT"

    discount_name = models.CharField(max_length=200)
    dicount_type = models.CharField(
        max_length=200, choices=DiscountType.choices, default=DiscountType.PERCENTAGE
    )
    discount_amount = models.FloatField()
