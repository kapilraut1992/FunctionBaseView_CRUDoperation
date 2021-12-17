from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        labels={
            'model_name':'PRODUCT MODEL NAME',
            'ram':'SYSTEM RAM CAPACITY(GB) ',
            'rom':'SYSTEM ROM CAPACITY(GB) ',
            'processor':'PROCESSOR (GHz)',
            'price':'PRICE',
            'weight':'PRODUCT WEIGHT(Kgrm)'
        }








    # model_name=forms.CharField(max_length=50)
    # ram=forms.IntegerField()
    # rom=forms.FloatField()
    # processor=forms.FloatField()
    # price=forms.FloatField()
    # weight=forms.FloatField()