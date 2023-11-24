from re import I
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    code=models.CharField(max_length=100,blank=True, null=True)
    name=models.CharField(max_length=250,blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    part_number = models.CharField(max_length=100, blank=True, null=True)
    drawing_no = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    material_2 = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=4000, blank=True, null=True)
    packaging_length = models.FloatField(blank=True, null=True)
    packaging_wide = models.FloatField(blank=True, null=True)
    welment_profile_length = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    surface_area = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    picture = models.ImageField(default="../media/default/no-photos.png", blank=True, null=True)

    category = models.ForeignKey(Category, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.part_number + ' - ' + self.description

    def count_inventory(self):
        stocks = Stock.objects.filter(product = self)
        stockIn = 0
        stockOut = 0
        for stock in stocks:
            if stock.type == '1':
                stockIn = int(stockIn) + int(stock.quantity)
            else:
                stockOut = int(stockOut) + int(stock.quantity)
        available  = stockIn - stockOut
        return available

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    type = models.CharField(max_length=2,choices=(('1','Stock-in'),('2','Stock-Out')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.part_number + ' - ' + self.product.description

class Invoice(models.Model):
    transaction = models.CharField(max_length = 250)
    customer = models.CharField(max_length = 250)
    total = models.FloatField(default= 0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction

    def item_count(self):
        return Invoice_Item.objects.filter(invoice = self).aggregate(Sum('quantity'))['quantity__sum']

class Invoice_Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank= True, null= True)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.invoice.transaction


@receiver(models.signals.post_save, sender=Invoice_Item)
def stock_update(sender, instance, **kwargs):
    stock = Stock(product = instance.product, quantity = instance.quantity, type = 2)
    stock.save()
    # stockID = Stock.objects.last().id
    Invoice_Item.objects.filter(id= instance.id).update(stock=stock)

@receiver(models.signals.post_delete, sender=Invoice_Item)
def delete_stock(sender, instance, **kwargs):
    try:
        stock = Stock.objects.get(id=instance.stock.id).delete()
    except:
        return instance.stock.id

class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title