from django.db import models
from django.urls import reverse


class Product(models.Model):
    """
    Product
    """
    name = models.CharField(max_length=256, help_text="Name", verbose_name="Name")
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", help_text="Related categories", blank=True, related_name="products")

    class Meta:
        ordering = ["id", "name", "brand"]

    def __str__(self) -> str:
        """
        String representation of the Product instance
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url for a particular Product instance
        """
        return reverse('product-detail', args=[str(self.id)])
