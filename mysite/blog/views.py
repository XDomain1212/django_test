from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
class People(object):
    def __init__(self,name:str,age:str,sex:str):
        self.name=name
        self.age=age
        self.sex=sex

def index(request):
    # context={'title':'My Django page','name':'Lee Min','age':'39','sex':'male'}
    lm=People('lee min','39','male')
    # template=loader.get_template("blog/templates/index.html")
    return render(request,'blog/templates/index.html',context={'name':lm.name,'age':lm.age,'sex':lm.sex})
    