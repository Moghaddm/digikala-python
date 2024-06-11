from typing import Any
from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','description']
        ordering = ['price']
        
    def clean(self):
        cleaned_data = self.cleaned_data
        
        print(cleaned_data.get('name'))
        
        if len(cleaned_data.get('name')) < 2: 
            self.add_error('name','cannot set name of product less than 2 charachters.')
        # if len(cleaned_data['description']) < 5:
        #     self.add_error('description','cannot set description of product less than 5 charachters.')
            
        return cleaned_data    
        

class ProductFormOld(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.IntegerField()
    
    def clean_price(self):
        cleaned_data = self.cleaned_data
        price =  cleaned_data['price']
        if price < 1000:
            raise forms.ValidationError("invalid price.")
        return price
    
    def clean(self):
        cleaned_data = self.cleaned_data
        
        print(cleaned_data.get('name'))
        
        if len(cleaned_data.get('name')) < 2: 
            self.add_error('name','cannot set name of product less than 2 charachters.')
        if len(cleaned_data['description']) < 5:
            self.add_error('description','cannot set description of product less than 5 charachters.')
            
        return cleaned_data    
        