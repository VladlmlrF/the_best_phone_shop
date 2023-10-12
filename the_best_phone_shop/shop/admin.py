from django.contrib import admin
from .models import Manufacturer, Product


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'manufacturer', 'price', 'color', 'memory', 'cpu', 'display_diagonal',
                    'available', 'created', 'updated']
    list_filter = ['manufacturer', 'name', 'memory', 'color']
    list_editable = ['price', 'available']
    search_fields = ['name', 'memory', 'color']
    prepopulated_fields = {'slug': ('name', 'memory', 'color')}
