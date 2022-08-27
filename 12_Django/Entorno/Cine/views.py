from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
from .models import Director
"""

def index(request):
    directores = Director.objects.all()
    return render(request,'index.html')#,context=directores)
"""



def index(request):
  template = loader.get_template('index.html')
  directores = Director.objects.all()
  context = {'directores':directores}
  return HttpResponse(template.render(context,request))