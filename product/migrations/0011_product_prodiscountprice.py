# Generated by Django 4.1.3 on 2022-12-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_proslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProDiscountPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Product Price'),
            preserve_default=False,
        ),
    ]
