from WebApp.models import *
from django import forms
from django.forms import ModelForm

class CompanyForm(ModelForm):
    class Meta:
        model = FP
        fields = ['bin_fp','kvartal','date','bs','summa','priznak']


class BSForm(ModelForm):
    class Meta:
        model = BS
        fields = ['kod','name']

class CompBankForm(ModelForm):
     class Meta:
        model = PB
        fields = ['bin_pb','bank', 'schet']

class BankForm(ModelForm):
     class Meta:
        model = Bank
        fields = ['name','address']
