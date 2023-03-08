from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Product category
    """
    name = models.CharField(max_length=256, help_text="Name", verbose_name="Name")

    class Meta:
        ordering = ["id", "name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        """
        String representation of the Category instance
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url for a particular Category instance
        """
        return reverse('category-detail', args=[str(self.id)])
