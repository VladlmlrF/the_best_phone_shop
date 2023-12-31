# Generated by Django 4.2.6 on 2023-10-12 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'manufacturer',
                'verbose_name_plural': 'manufacturers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=50)),
                ('memory', models.PositiveIntegerField()),
                ('cpu', models.CharField(max_length=100)),
                ('ram', models.PositiveIntegerField()),
                ('display_diagonal', models.FloatField()),
                ('display_resolution_height', models.PositiveIntegerField()),
                ('display_resolution_width', models.PositiveIntegerField()),
                ('display_refresh_rate', models.PositiveIntegerField()),
                ('matrix_type', models.CharField(choices=[('oled', 'OLED'), ('ips', 'IPS')], max_length=20)),
                ('camera', models.CharField(max_length=255)),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('thickness', models.FloatField()),
                ('weight', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.manufacturer')),
            ],
            options={
                'ordering': ['-price'],
            },
        ),
        migrations.AddIndex(
            model_name='manufacturer',
            index=models.Index(fields=['name'], name='shop_manufa_name_c1583f_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id', 'slug'], name='shop_produc_id_f21274_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='shop_produc_name_a2070e_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name', 'memory'], name='shop_produc_name_d87b80_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name', 'memory', 'color'], name='shop_produc_name_da9c1d_idx'),
        ),
    ]
