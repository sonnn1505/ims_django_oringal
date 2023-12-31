from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm

from django.contrib.auth.models import User
from more_itertools import quantify
from .models import Category, Product, Stock, Invoice, Invoice_Item, Image, Warehouse
from datetime import datetime

class UserRegistration(UserCreationForm):
    email = forms.EmailField(max_length=250,help_text="The email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')
    

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")


class UpdateProfile(UserChangeForm):
    username = forms.CharField(max_length=250,help_text="The Username field is required.")
    email = forms.EmailField(max_length=250,help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username','first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Password is Incorrect")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")

class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Confirm New Password")
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length="250")
    description = forms.Textarea()
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])

    class Meta:
        model = Category
        fields = ('name','description','status')

    def clean_name(self):
        id = self.instance.id if self.instance.id else 0
        name = self.cleaned_data['name']
        # print(int(id) > 0)
        # raise forms.ValidationError(f"{name} Category Already Exists.")
        try:
            if int(id) > 0:
                category = Category.objects.exclude(id=id).get(name = name)
            else:
                category = Category.objects.get(name = name)
        except:
            return name
            # raise forms.ValidationError(f"{name} Category Already Exists.")
        raise forms.ValidationError(f"{name} Category Already Exists.")

class SaveWarehouse(forms.ModelForm):
    code = forms.CharField(max_length="250")
    name = forms.CharField(max_length="250")
    address = forms.CharField(max_length="250")
    manager = forms.CharField(max_length="250")
    phone = forms.CharField(max_length="250")
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])

    class Meta:
        model = Warehouse
        fields = ('code','name','address','manager','phone')

    def clean_code(self):
        id = self.instance.id if self.instance.id else 0
        code = self.cleaned_data['code']
        # print(int(id) > 0)
        # raise forms.ValidationError(f"{name} Category Already Exists.")
        try:
            if int(id) > 0:
                warehouse = Warehouse.objects.exclude(id=id).get(code = code)
            else:
                warehouse = Warehouse.objects.get(code = code)
        except:
            return code
            # raise forms.ValidationError(f"{name} Category Already Exists.")
        raise forms.ValidationError(f"{code} Warehouse Already Exists.")


class SaveProduct(forms.ModelForm):
    name = forms.CharField(max_length="250", required= False)
    
    category            = forms.CharField(max_length=100, required=False)
    product_category    = forms.CharField(max_length=100, required=False)
    part_number         = forms.CharField(max_length=100, required=False)
    drawing_no          = forms.CharField(max_length=100, required=False)
    picture             = forms.CharField(max_length=100, required=False)
    description         = forms.CharField(max_length=4000,required=False)
    description_2       = forms.CharField(max_length=4000,required=False)
    material            = forms.CharField(max_length=100,required=False)
    demand_quantity     = forms.IntegerField(required=False)
    Specification       = forms.CharField(max_length=100,required=False)
    color               = forms.CharField(max_length=100,required=False)
    standard            = forms.CharField(max_length=100,required=False)
    model               = forms.CharField(max_length=100,required=False)
    maker               = forms.CharField(max_length=100,required=False)
    origin              = forms.CharField(max_length=100,required=False)
    heat_treatment      = forms.CharField(max_length=100,required=False)
    surface_protection  = forms.CharField(max_length=100,required=False)
    suface_finish       = forms.CharField(max_length=100,required=False)
    comment             = forms.CharField(max_length=4000, required=False)
    welment_profile_length = forms.CharField(required=False)
    weight                 = forms.CharField(required=False)
    status              = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])
    class Meta:
        model = Product
        fields = ('category'
                    ,'product_category'
                    ,'part_number'
                    ,'drawing_no'
                    ,'picture'
                    ,'description'
                    ,'description_2'
                    ,'material'
                    ,'demand_quantity'
                    ,'Specification'
                    ,'color'
                    ,'standard'
                    ,'model'
                    ,'maker'
                    ,'origin'
                    ,'heat_treatment'
                    ,'surface_protection'
                    ,'suface_finish'
                    ,'comment'
                    ,'welment_profile_length'
                    ,'weight'
                    ,'status'
                  )

    # def clean_code(self):
    #     id = self.instance.id if self.instance.id else 0
    #     code = self.cleaned_data['code']
    #     try:
    #         if int(id) > 0:
    #             product = Product.objects.exclude(id=id).get(code = code)
    #         else:
    #             product = Product.objects.get(code = code)
    #     except:
    #         return code
    #     raise forms.ValidationError(f"{code} Category Already Exists.")

    def clean_price(self):
        price = 1
        return price
    
    def clean_category(self):
        pid = self.cleaned_data['category']
        try:
            category = Category.objects.get(id=pid)
            return category
        except:
            raise forms.ValidationError("category is not valid")
        
    def clean_picture(self):
        pid = self.cleaned_data['picture']
        try:
            picture = self.cleaned_data['part_number'] +'.JPG'
            return picture or None
        except:
            raise forms.ValidationError("picture is not valid")

class SaveStock(forms.ModelForm):
    product = forms.CharField(max_length=30)
    quantity = forms.CharField(max_length=250)
    type = forms.ChoiceField(choices=[('1','Stock-in'),('2','Stock-Out')])

    class Meta:
        model = Stock
        fields = ('product', 'quantity', 'type')

    def clean_product(self):
        pid = self.cleaned_data['product']
        try:
            product = Product.objects.get(id=pid)
            print(product)
            return product
        except:
            raise forms.ValidationError("Product is not valid")

class SaveInvoice(forms.ModelForm):
    transaction = forms.CharField(max_length=100)
    customer = forms.CharField(max_length=250)
    total = forms.FloatField()
    type= forms.IntegerField()
    class Meta:
        model = Invoice
        fields = ('transaction', 'customer', 'total','type')

    def clean_transaction(self):
        pref = datetime.today().strftime('%Y%m%d')
        transaction= ''
        code = str(1).zfill(4)
        while True:
            invoice = Invoice.objects.filter(transaction=str(pref + code)).count()
            if invoice > 0:
                code = str(int(code) + 1).zfill(4)
            else:
                transaction = str(pref + code)
                break
        return transaction

class SaveInvoiceItem(forms.ModelForm):
    invoice = forms.CharField(max_length=30)
    product = forms.CharField(max_length=30)
    quantity = forms.CharField(max_length=100)
    price = forms.CharField(max_length=100)
    warehouse = forms.CharField(max_length=30)

    class Meta:
        model = Invoice_Item
        fields = ('invoice','product','quantity','price','warehouse')

    def clean_invoice(self):
        iid = self.cleaned_data['invoice']
        try:
            invoice = Invoice.objects.get(id=iid)
            return invoice
        except:
            raise forms.ValidationError("Invoice ID is not valid")

    def clean_product(self):
        pid = self.cleaned_data['product']
        try:
            product = Product.objects.get(id=pid)
            return product
        except:
            raise forms.ValidationError("Product is not valid")

    def clean_quantity(self):
        qty = self.cleaned_data['quantity']
        if qty.isnumeric():
            return int(qty)
        raise forms.ValidationError("Quantity is not valid")
    
    def clean_warehouse(self):
        pid = self.cleaned_data['warehouse']
        try:
            warehouse = Warehouse.objects.get(id=pid)
            return warehouse
        except:
            raise forms.ValidationError("Warhouse is not valid")
    

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

