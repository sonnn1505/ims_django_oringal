# Generated by Django 4.0.3 on 2023-11-20 11:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0007_invoice_date_created_invoice_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='imsApp.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='comment',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='drawing_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='packaging_length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='packaging_wide',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='part_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='surface_area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='welment_profile_length',
            field=models.FloatField(blank=True, null=True),
        ),
    ]