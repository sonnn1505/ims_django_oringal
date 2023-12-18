# Generated by Django 4.0.3 on 2023-12-08 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0018_alter_invoice_item_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_item',
            name='warehouse',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='imsApp.warehouse'),
        ),
    ]