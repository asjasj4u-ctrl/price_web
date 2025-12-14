from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="المنتج")
    regular_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="السعر العادي"
    )
    dukkan = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="الدكان")
    kian = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="كيان")
    competitor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="المنافس")
    othaim = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="العثيم")
    amazon = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="أمازون")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="آخر تحديث")

    def get_min_price(self):
        prices = [p for p in [self.dukkkan, self.kian, self.competitor, self.othaim, self.amazon] if p is not None]
        return min(prices) if prices else None

    def __str__(self):
        return self.name
