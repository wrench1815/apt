from django.db import models
from django.utils import timezone


class Product(models.Model):
    """Model definition for Product."""

    name = models.TextField()
    price = models.CharField(max_length=20)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return str(self.name)
