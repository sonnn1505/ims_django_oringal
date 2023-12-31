# Generated by Django 4.0.3 on 2023-12-08 09:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0016_alter_product_comment_alter_product_description_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=400)),
                ('manager', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='invoice_item',
            name='warehouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='imsApp.warehouse',db_constraint=False),
            preserve_default=False,
        ),
    ]
