from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def basic(request):
     companies = Predpriyatie.objects.all()
     nk = NK.objects.all()
     banki = Bank.objects.all()

     return render(request, "WebApp/index.html", {"companies": companies,"nk": nk, "banki": banki})

def workers(request):
    
    fp = FP.objects.all()
    form = CompanyForm()
    if request.method=='POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save() 
            form=CompanyForm()  
    return render(request, "WebApp/workers.html", {"form":form, "fp":fp})

def delete(request, id):
        fp = FP.objects.get(pk=id)
        fp.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def workers_1(request):
    bs = BS.objects.all()
    form = BSForm()
    if request.method=='POST':
        form = BSForm(request.POST)
        if form.is_valid():
            form.save() 
            form=BSForm()  
    return render(request, "WebApp/workers_1.html", {"form":form, "bs":bs})

def delete_1(request, id):
        bs = BS.objects.get(pk=id)
        bs.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def workers_2(request):
    banks = Bank.objects.all()
    form = BankForm()
    if request.method=='POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save() 
            form=BankForm()  
    return render(request, "WebApp/workers_2.html", {"form":form, "banks":banks})

def delete_2(request, id):
        banks = Bank.objects.get(pk=id)
        banks.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def workers_3(request):
    cbf = PB.objects.all()
    form = CompBankForm()
    if request.method=='POST':
        form = CompBankForm(request.POST)
        if form.is_valid():
            form.save() 
            form=CompBankForm()  
    return render(request, "WebApp/workers_3.html", {"form":form, "cbf":cbf})

def delete_3(request, id):
        cbf = PB.objects.get(pk=id)
        cbf.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    
# def bs_form(request):
#     form_bs = BSForm()
#     if request.method=='POST' and 'btnform2' in request.POST:
#         form_bs = BSForm(request.POST)
#         if form_bs.is_valid():
#             form_bs.save() 
#             form_bs=BSForm()  

#     return render(request, "", {"form":form}, {"form_bs":form_bs} )


