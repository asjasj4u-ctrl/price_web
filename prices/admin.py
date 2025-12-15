from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'regular_price', 'dukkan', 'kian', 'competitor', 'othaim', 'amazon')
    readonly_fields = ('name', 'regular_price')  # الحقول الثابتة غير قابلة للتعديل
