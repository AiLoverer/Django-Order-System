from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    '''项目前台大堂点餐首页'''
    return render(request,"web/index.html")