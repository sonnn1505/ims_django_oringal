# Generated by Django 4.0.3 on 2023-11-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0012_alter_product_suface_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='welment_profile_length',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
