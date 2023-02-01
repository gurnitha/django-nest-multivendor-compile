# Generated by Django 3.2 on 2023-01-04 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodim_image', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('prodim_created', models.DateTimeField(auto_now_add=True)),
                ('prodim_updated', models.DateTimeField(blank=True, null=True)),
                ('prodim_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product')),
            ],
            options={
                'verbose_name_plural': 'Product images',
            },
        ),
    ]
