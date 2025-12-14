from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    dukkan = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    kian = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    competitor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    othaim = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amazon = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
