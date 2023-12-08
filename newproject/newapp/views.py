from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect
from django.template import loader
from newapp.models import Home
from django.urls import reverse
# Create your views here.
def index(request):
    myhome = Home.objects.all().values()
    template = loader.get_template('form.html')
    context={
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))

def abc(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        fathername=request.POST.get('fathername')
        mothername=request.POST.get('mothername')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        address=request.POST.get('address')
        fathermobileno=request.POST.get('fathermobileno')
        mothermobileno=request.POST.get('mothermobileno')
        a=Home(firstname=firstname,lastname=lastname,fathername=fathername,mothername=mothername,dob=dob,age=age,address=address,fathermobileno=fathermobileno,mothermobileno=mothermobileno)
        a.save()
    return render(request,"form.html")

def delete(request,area):
    myhome=Home.objects.get(area=area)
    myhome.delete()
    return HttpResponsePermanentRedirect(reverse('index'))

def update(request,mobilenumber):
    myhome=Home.objects.get(mobilenumber=mobilenumber)
    template =loader.get_template('update.html')
    context = {
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,mobilenumber):
    mobilenumber=request.POST['mobilenumber']
    home=Home.objects.get(mobilenumber=mobilenumber)
    home.mobilenumber=mobilenumber
    home.save()
    return HttpResponsePermanentRedirect(reverse('index'))
