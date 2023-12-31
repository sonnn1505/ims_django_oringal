from email import message
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from ims_django.settings import MEDIA_ROOT, MEDIA_URL
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from imsApp.forms import *
from imsApp.models import *
from cryptography.fernet import Fernet
from django.conf import settings
import base64
import openpyxl
import pandas as pd
from django.shortcuts import render
import datetime
from django.http import JsonResponse
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

context = {
    'page_title' : 'File Management System',
}
#login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
                logger.warning(str(datetime.datetime.now())+' Login success')
            else:
                resp['msg'] = "Incorrect username or password"
                logger.warning(str(datetime.datetime.now())+' Login Incorrect username or password')
        else:
            resp['msg'] = "Incorrect username or password"
            logger.warning(str(datetime.datetime.now())+' Login Incorrect username or password')
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required
def home(request):
    context['page_title'] = 'Home'
    context['categories'] = Category.objects.count()
    context['products'] = Product.objects.count()
    context['sales'] = Invoice.objects.count()
    logger.warning(str(datetime.datetime.now())+' Home Accessed')
    return render(request, 'home.html',context)

def registerUser(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home-page')
    context['page_title'] = "Register User"
    if request.method == 'POST':
        data = request.POST
        form = UserRegistration(data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            loginUser = authenticate(username= username, password = pwd)
            login(request, loginUser)
            return redirect('home-page')
        else:
            context['reg_form'] = form

    return render(request,'register.html',context)

@login_required
def update_profile(request):
    context['page_title'] = 'Update Profile'
    user = User.objects.get(id = request.user.id)
    if not request.method == 'POST':
        form = UpdateProfile(instance=user)
        context['form'] = form
        print(form)
    else:
        form = UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated")
            return redirect("profile")
        else:
            context['form'] = form
            
    return render(request, 'manage_profile.html',context)


@login_required
def update_password(request):
    context['page_title'] = "Update Password"
    if request.method == 'POST':
        form = UpdatePasswords(user = request.user, data= request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Account Password has been updated successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
        else:
            context['form'] = form
    else:
        form = UpdatePasswords(request.POST)
        context['form'] = form
    return render(request,'update_password.html',context)


@login_required
def profile(request):
    context['page_title'] = 'Profile'
    return render(request, 'profile.html',context)


# WareHouse
@login_required
def warehouse_mgt(request):
    context['page_title'] = "Warehouse"
    warehouse = Warehouse.objects.all()
    context['warehouse'] = warehouse
    logger.warning(str(datetime.datetime.now())+' warehouse Accessed')
    return render(request, 'warehouse_mgt.html', context)

# Category
@login_required
def category_mgt(request):
    context['page_title'] = "Product Categories"
    categories = Category.objects.all()
    context['categories'] = categories
    logger.warning(str(datetime.datetime.now())+' category Accessed')
    return render(request, 'category_mgt.html', context)

@login_required
def save_category(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            category = Category.objects.get(pk=request.POST['id'])
        else:
            category = None
        if category is None:
            form = SaveCategory(request.POST)
        else:
            form = SaveCategory(request.POST, instance= category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been saved successfully.')
            resp['status'] = 'success'
            logger.warning(str(datetime.datetime.now())+' save_category has been saved successfully.')
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
                    logger.warning(str(datetime.datetime.now())+' save_category error form ' + str(error))
    else:
        resp['msg'] = 'No data has been sent.'
        logger.warning(str(datetime.datetime.now())+' save_category No data has been sent. ')
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def save_warehouse(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            warehouse = Warehouse.objects.get(pk=request.POST['id'])
        else:
            warehouse = None
        if warehouse is None:
            form = SaveWarehouse(request.POST)
        else:
            form = SaveWarehouse(request.POST, instance= warehouse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Warehouse has been saved successfully.')
            resp['status'] = 'success'
            logger.warning(str(datetime.datetime.now())+' save warehouse has been saved successfully.')
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
                    logger.warning(str(datetime.datetime.now())+' save warehouse error form ' + str(error))
    else:
        resp['msg'] = 'No data has been sent.'
        logger.warning(str(datetime.datetime.now())+' save warehouse No data has been sent. ')
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def delete_warehouse(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            warehouse = Warehouse.objects.get(id = request.POST['id'])
            warehouse.delete()
            messages.success(request, 'Warehouse has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'Warehouse has failed to delete'
            logger.warning(str(datetime.datetime.now())+' delete warehouse ' + str(err))

    else:
        resp['msg'] = 'Category has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def manage_category(request, pk=None):
    context['page_title'] = "Manage Category"
    if not pk is None:
        category = Category.objects.get(id = pk)
        context['category'] = category
    else:
        context['category'] = {}

    return render(request, 'manage_category.html', context)

@login_required
def manage_warehouse(request, pk=None):
    context['page_title'] = "Manage Warehouse"
    if not pk is None:
        warehouse = Warehouse.objects.get(id = pk)
        context['warehouse'] = warehouse
    else:
        context['warehouse'] = {}

    return render(request, 'manage_warehouse.html', context)


@login_required
def delete_category(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            category = Category.objects.get(id = request.POST['id'])
            category.delete()
            messages.success(request, 'Category has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'Category has failed to delete'
            logger.warning(str(datetime.datetime.now())+' delete_category ' + str(err))

    else:
        resp['msg'] = 'Category has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")
        
# product
@login_required
def product_mgt(request):
    context['page_title'] = "Product List"
    products = Product.objects.all()
    context['products'] = products

    return render(request, 'product_mgt.html', context)

@login_required
def save_product(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            product = Product.objects.get(pk=request.POST['id'])
        else:
            product = None
        if product is None:
            form = SaveProduct(request.POST)
        else:
            form = SaveProduct(request.POST, instance= product)
        if form.is_valid():
            form.save()
            # upload picture
            file = request.FILES['picture_file']
            new_file = Files(file = file)
            new_file.save()
            # upload picture
            messages.success(request, 'Product has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def manage_product(request, pk=None):
    context['page_title'] = "Manage Product"
    category_list = Category.objects.all()
    context['category_list'] = category_list
    if not pk is None:
        product = Product.objects.get(id = pk)
        context['product'] = product
        context['edit'] = '1'
    else:
        context['edit'] = '0'
        context['product'] = {}

    return render(request, 'manage_product.html', context)

@login_required
def manage_product_import(request):
    context['page_title'] = "Manage Product Import"
    return render(request, 'manage_product_import.html', context)

@login_required
def import_data_to_db(request):
    if "GET" == request.method:
        return render(request, 'manage_product_import', {})
    else:
        excel_file = request.FILES["files"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        df_tm = worksheet.values
        coluna_tm = next(df_tm)[0:]

        #start validate schema excel file
        colum_need = ('stt', 'category', 'product_category', 'part_number'\
                      , 'drawing_no', 'picture', 'description', 'description_2'\
                      , 'material', 'demand_quantity', 'Specification', 'color'\
                      , 'standard', 'model', 'maker', 'origin', 'heat_treatment'\
                      , 'surface_protection', 'suface_finish', 'comment'\
                      , 'welment_profile_length', 'weight')
        temp3 = []
        for element in coluna_tm:
            if element not in colum_need:
                temp3.append(element)
        if len(temp3) >0:
            context['error_mgs'] = "columns header in file: [" + ', '.join(temp3) + '] are Not Validate the Names'
            return render(request, 'manage_product_import.html', context)

        #end validate schema excel file

        df = pd.DataFrame(df_tm, columns=coluna_tm)
        print(df.head())
        df['demand_quantity'].fillna(0, inplace=True)
        df = df.fillna('')
    
        for index, row in df.iterrows():
            part_num_tmpl = row['part_number']
            if part_num_tmpl is not None:
                if Product.objects.filter(part_number = part_num_tmpl).exists():
                    prd = Product.objects.get(part_number = part_num_tmpl)
                    prd.demand_quantity = prd.demand_quantity + row['demand_quantity']
                    prd.save()
                else:
                    product = Product()
                    cat =  row['category']
                    if Category.objects.filter(name = cat).exists():
                        category = Category.objects.get(name = row['category'])
                        product.category = category
                        product.part_number = part_num_tmpl
                        product.product_category = row['product_category']
                        product.drawing_no = row['drawing_no']
                        product.description = row['description']
                        product.description_2 = row['description_2']
                        product.material = row['material']
                        product.picture = str(row['part_number']) + '.JPG'
                        product.demand_quantity = row['demand_quantity']
                        product.Specification = row['Specification']
                        product.color = row['color']
                        product.standard = row['standard']
                        product.model = row['model']
                        product.maker = row['maker']
                        product.origin = row['origin']
                        product.heat_treatment = row['heat_treatment']
                        product.surface_protection = row['surface_protection']
                        product.suface_finish = row['suface_finish']
                        product.comment = row['comment']
                        product.welment_profile_length = row['welment_profile_length']
                        product.weight = row['weight']
                        product.save()
 
        # data_to_display = df.to_html()
    return redirect('product-page')
   
@login_required
def delete_product(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            product = Product.objects.get(id = request.POST['id'])
            product.delete()
            messages.success(request, 'Product has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'Product has failed to delete'
            logger.warning(str(datetime.datetime.now())+' delete_product No ' + str(err))

    else:
        resp['msg'] = 'Product has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")

#Inventory
@login_required
def inventory(request):
    context['page_title'] = 'Inventory'

    products = Product.objects.all()
    context['products'] = products

    return render(request, 'inventory.html', context)

#Inventory History
@login_required
def inv_history(request, pk= None):
    context['page_title'] = 'Inventory History'
    if pk is None:
        messages.error(request, "Product ID is not recognized")
        return redirect('inventory-page')
    else:
        product = Product.objects.get(id = pk)
        stocks = Stock.objects.filter(product = product).all()
        context['product'] = product
        context['stocks'] = stocks

        return render(request, 'inventory-history.html', context )

#Stock Form
@login_required
def manage_stock(request,pid = None ,pk = None):
    if pid is None:
        messages.error(request, "Product ID is not recognized")
        return redirect('inventory-page')
    context['pid'] = pid
    if pk is None:
        context['page_title'] = "Add New Stock"
        context['stock'] = {}
    else:
        context['page_title'] = "Manage New Stock"
        stock = Stock.objects.get(id = pk)
        context['stock'] = stock
    
    return render(request, 'manage_stock.html', context )

@login_required
def save_stock(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            stock = Stock.objects.get(pk=request.POST['id'])
        else:
            stock = None
        if stock is None:
            form = SaveStock(request.POST)
        else:
            form = SaveStock(request.POST, instance= stock)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def delete_stock(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            stock = Stock.objects.get(id = request.POST['id'])
            stock.delete()
            messages.success(request, 'Stock has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'Stock has failed to delete'
            logger.warning(str(datetime.datetime.now())+' delete_stock ' + str(err))

    else:
        resp['msg'] = 'Stock has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def sales_mgt(request):
    context['page_title'] = 'Sales'
    products = Product.objects.filter(status = 1).all()
    context['products'] = products
    warehouse = Warehouse.objects.all()
    context['warehouses'] = warehouse
    return render(request,'sales.html', context)

@login_required
def buy_mgt(request):
    context['page_title'] = 'Buy'
    products = Product.objects.filter(status = 1).all()
    context['products'] = products
    warehouse = Warehouse.objects.all()
    context['warehouses'] = warehouse
    return render(request,'buy.html', context)


def get_product(request,pk = None):
    resp = {'status':'failed','data':{},'msg':''}
    if pk is None:
        resp['msg'] = 'Product ID is not recognized'
    else:
        product = Product.objects.get(id = pk)
        resp['data']['product'] = str(product.part_number + " - " + product.description)
        resp['data']['id'] = product.id
        resp['data']['price'] = product.price
        resp['status'] = 'success'
    
    return HttpResponse(json.dumps(resp),content_type="application/json")

def save_buy(request):
    resp = {'status':'failed', 'msg' : ''}
    id = 2
    if request.method == 'POST':
        pids = request.POST.getlist('pid[]')
        wh = request.POST.get('warehouse[]')[0]
        invoice_form = SaveInvoice(request.POST)
        if invoice_form.is_valid():
            invoice_form.save()
            invoice = Invoice.objects.last()
            for pid in pids:
                data = {
                    'invoice':invoice.id,
                    'product':pid,
                    'quantity':request.POST['quantity['+str(pid)+']'],
                    'price':request.POST['price['+str(pid)+']'],
                    'warehouse':wh
                }
                print(data)
                ii_form = SaveInvoiceItem(data=data)
                print(ii_form.data)
                if ii_form.is_valid():
                    ii_form.save()
                else:
                    for fields in ii_form:
                        for error in fields.errors:
                            resp['msg'] += str(error + "<br>")
                    break
            messages.success(request, "Sale Transaction has been saved.")
            resp['status'] = 'success'
            # invoice.delete()
        else:
            for fields in invoice_form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")

    return HttpResponse(json.dumps(resp),content_type="application/json")


def save_sales(request):
    resp = {'status':'failed', 'msg' : ''}
    id = 2
    if request.method == 'POST':
        pids = request.POST.getlist('pid[]')
        wh = request.POST.get('warehouse[]')[0]
        invoice_form = SaveInvoice(request.POST)
        if invoice_form.is_valid():
            invoice_form.save()
            invoice = Invoice.objects.last()
            for pid in pids:
                data = {
                    'invoice':invoice.id,
                    'product':pid,
                    'quantity':request.POST['quantity['+str(pid)+']'],
                    'price':request.POST['price['+str(pid)+']'],
                    'warehouse':wh
                }
                print(data)
                ii_form = SaveInvoiceItem(data=data)
                # print(ii_form.data)
                if ii_form.is_valid():
                    ii_form.save()
                else:
                    for fields in ii_form:
                        for error in fields.errors:
                            resp['msg'] += str(error + "<br>")
                    break
            messages.success(request, "Sale Transaction has been saved.")
            resp['status'] = 'success'
            # invoice.delete()
        else:
            for fields in invoice_form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")

    return HttpResponse(json.dumps(resp),content_type="application/json")

@login_required
def invoices(request):
    invoice =  Invoice.objects.all()
    context['page_title'] = 'Invoices'
    context['invoices'] = invoice

    return render(request, 'invoices.html', context)

@login_required
def delete_invoice(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            invoice = Invoice.objects.get(id = request.POST['id'])
            invoice.delete()
            messages.success(request, 'Invoice has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'Invoice has failed to delete'
            print(err)

    else:
        resp['msg'] = 'Invoice has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for file in files:
            new_file = Files(
                file = file
            )
            new_file.save()
        return redirect('product-page')
    else:
        form = ImageForm()
        return render(request, 'manage_product_import_photos.html', {'form': form})

# chart
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
colorPalette = ["#55efc4", "#81ecec", "#a29bfe", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8"]
colorPrimary, colorSuccess, colorDanger = "#79aec8", colorPalette[0], colorPalette[5]


def get_year_dict():
    year_dict = dict()

    for month in months:
        year_dict[month] = 0

    return year_dict


def generate_color_palette(amount):
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette

@login_required
def get_filter_options(request):
    stock_list = Stock.objects.annotate(year=ExtractYear("date_created")).values("year").order_by("-year").distinct()

    options = [stock["year"] for stock in stock_list]

    return JsonResponse({
        "options": options,
    })

@login_required
def get_inventory_line_year(request, year):

    stocks = Stock.objects.filter(date_created__year = year)
    grouped_stock_in = stocks.annotate(quantity_sum=F("quantity")).annotate(month=ExtractMonth("date_created"))\
        .values("month").annotate(average=Sum("quantity")).values("month", "average").filter(type = '1').order_by("month")
    
    grouped_stock_out = stocks.annotate(quantity_sum=F("quantity")).annotate(month=ExtractMonth("date_created"))\
        .values("month").annotate(average=Sum("quantity")).values("month", "average").filter(type = '2').order_by("month")
    
    stock_dict_in = get_year_dict()

    for group in grouped_stock_in:
        stock_dict_in[months[group["month"]-1]] = round(group["average"], 2)

    stock_dict_out = get_year_dict()

    for group in grouped_stock_out:
        stock_dict_out[months[group["month"]-1]] = round(group["average"], 2)
    
    return JsonResponse({
        "title": f"stock in {year}",
        "data": {
            "labels": list(stock_dict_in.keys()),
            "datasets": [
                {
                "label": "Total Quantity Import",
                "backgroundColor": colorSuccess,
                "borderColor": colorSuccess,
                "data": list(stock_dict_in.values()),
                }
                ,  {
                "label":"Total Quantity Export",
                "backgroundColor":colorDanger,
                "borderColor": colorDanger,
                "data": list(stock_dict_out.values()),
                }
            ]
        },
    })

@login_required
def get_inventory_pie_year(request, year):

    stock = Stock.objects.filter(date_created__year=year)

    sum_stock_in = stock.filter(type='1').aggregate(Sum('quantity'))['quantity__sum']
    sum_stock_out = stock.filter(type='2').aggregate(Sum('quantity'))['quantity__sum']

    return JsonResponse({
        "title": f"Inventory in {year}",
        "data": {
            "labels": ["Import", "Export"],
            "datasets": [{
                "label": "Total Quantity Import",
                "backgroundColor": [colorSuccess, colorDanger],
                "borderColor": [colorSuccess, colorDanger],
                "data": [
                    sum_stock_in,
                    sum_stock_out,
                ],
            }]
        },
    })