from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render

def HomePage(request):
    # return HttpResponse('Hello ')
    return render(request,'base.html')