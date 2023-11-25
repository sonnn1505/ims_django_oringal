# Generated by Django 4.0.3 on 2023-11-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0010_product_demand_quantity_alter_product_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='material_2',
            new_name='Specification',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='packaging_length',
            new_name='suface_finish',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='packaging_wide',
            new_name='surface_protection',
        ),
        migrations.RemoveField(
            model_name='product',
            name='surface_area',
        ),
        migrations.RemoveField(
            model_name='product',
            name='volume',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='heat_treatment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='maker',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='standard',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]