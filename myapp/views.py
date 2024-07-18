from django.shortcuts import render,redirect
from .models import products
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    return render(request,'addpage.html')

def additem(request):
    if request.method=='POST':
        name=request.POST['name']
        companyname=request.POST['companyname']
        price=request.POST['price']
        image=request.FILES.get('image')
        products(Name=name,Companyname=companyname,Price=price,Image=image).save()
        return redirect ('views')
    return render(request,'addpage.html')
        
def views(request):
    data=products.objects.all()
    return render(request,'view.html',{'data':data})

def details(request,id):
    data=products.objects.get(id=id)
    return render(request,'details.html',{'details':data})
def delete(request,id):
    data=products.objects.get(id=id)
    data.delete()
    return redirect('views')
def viewbutton(request):
    data=products.objects.all()
    return render(request,'view.html',{'data':data})

def update(request,id):
    data=products.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        companyname=request.POST['companyname']
        price=request.POST['price']
        image=request.FILES.get('image')
        data.Name=name
        data.Companyname=companyname
        data.Price=price
        data.Image=image
        data.save()
        return redirect('views')
    return render(request,'update.html',{'update':data})