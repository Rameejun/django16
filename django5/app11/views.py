from django.shortcuts import render
from app11.forms import *
from app11.models import *
# Create your views here.


def fun(request):
      form  = employeeform()
      if "eid" in request.GET:
             eid = request.GET['eid']
             name =request.GET['name']
             age = age = request.GET['age']
             employee.objects.create(eid = eid,name = name ,age = age)
      return render(request,"home/form1.html",{"form1":form})