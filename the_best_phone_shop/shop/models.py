from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_manufacturer', args=[self.slug])


class Product(models.Model):
    MATRIX_TYPES = (
        ('oled', 'OLED'),
        ('ips', 'IPS')
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    color = models.CharField(max_length=50)

    memory = models.PositiveIntegerField()
    cpu = models.CharField(max_length=100)
    ram = models.PositiveIntegerField()

    display_diagonal = models.FloatField()
    display_resolution_height = models.PositiveIntegerField()
    display_resolution_width = models.PositiveIntegerField()
    display_refresh_rate = models.PositiveIntegerField()
    matrix_type = models.CharField(choices=MATRIX_TYPES, max_length=20)

    camera = models.CharField(max_length=255)

    height = models.FloatField()
    width = models.FloatField()
    thickness = models.FloatField()

    weight = models.PositiveIntegerField()

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-price']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['name', 'memory']),
            models.Index(fields=['name', 'memory', 'color']),
        ]

    def __str__(self):
        return f'{self.name} {self.memory} {self.color}'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
