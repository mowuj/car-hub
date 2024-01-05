from django.shortcuts import render
from brand.models import Brand
from car.models import Car
def home(request):
    data=Brand.objects.all()
    car=Car.objects.all()
    return render(request,'home.html',{'data':data,'cars':car})