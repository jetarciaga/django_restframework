import uuid
from django.db import models


class Product(models.Model):
    """Store product model"""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural  = 'Products'


class Transaction(models.Model):
    """Transaction model"""
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    products = models.ManyToManyField(Product, through='TransactionItem')

    def total_price(self):
        total = sum(item.product.price * item.quantity for item in self.transactionitem_set.all())
        return total

    def __str__(self):
        return str(self.transaction_id)


class TransactionItem(models.Model):
    """Model that connects transaction and product"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"



