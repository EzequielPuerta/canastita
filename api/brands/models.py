from django.db import models
from django.urls import reverse


class Brand(models.Model):
    """
    Product brand
    """
    name = models.CharField(max_length=256, help_text="Name", verbose_name="Name")
    categories = models.ManyToManyField('Category', help_text="Related categories", related_name="brands")


    class Meta:
        ordering = ["id", "name"]


    def __str__(self) -> str:
        """
        String representation of the Brand instance
        """
        return self.name


    def get_absolute_url(self):
        """
        Returns the url for a particular Brand instance
        """
        return reverse('brand-detail', args=[str(self.id)])
