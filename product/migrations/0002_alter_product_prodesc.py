# Generated by Django 4.1.3 on 2022-12-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProDesc',
            field=models.TextField(),
        ),
    ]
