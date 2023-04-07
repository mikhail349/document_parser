from django.db import models


class Receipt(models.Model):
    """Модель чека."""

    shop_name = models.CharField(max_length=255)
    shop_physical_address = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    bank_card_number = models.CharField(max_length=19)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    category = models.CharField(max_length=255)
    potential_irrational_purchase = models.BooleanField()
    products_list = models.JSONField()
    english_description = models.JSONField()
