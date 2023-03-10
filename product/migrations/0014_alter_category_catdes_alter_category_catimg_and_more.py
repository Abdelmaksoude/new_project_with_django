# Generated by Django 4.1.3 on 2022-12-11 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0013_product_proisbestsaller_product_proisnew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATdes',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATimg',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATmain_category',
            field=models.CharField(max_length=50, verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATparent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATparent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='The Parent'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProCost',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProDesc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProName',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProPrice',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Probrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Procategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Proisbestsaller',
            field=models.BooleanField(default=False, verbose_name='Is The BestSaller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Proisnew',
            field=models.BooleanField(default=True, verbose_name='Is New'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Proslug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product Slug'),
        ),
        migrations.AlterField(
            model_name='productacsessories',
            name='PACCalternative',
            field=models.ManyToManyField(related_name='Acessoires', to='product.product', verbose_name='Product Alternative'),
        ),
        migrations.AlterField(
            model_name='productacsessories',
            name='PACCproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Name', to='product.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='productalternative',
            name='PALNalternative',
            field=models.ManyToManyField(related_name='Alternative_Product', to='product.product', verbose_name='Product Alternative'),
        ),
        migrations.AlterField(
            model_name='productalternative',
            name='PALNproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Main_Product', to='product.product', verbose_name='Product'),
        ),
    ]
