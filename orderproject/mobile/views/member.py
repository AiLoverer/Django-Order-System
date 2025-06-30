from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

# 移动端个人中心

def index(request):
    '''个人中心首页'''
    return render(request,"mobile/member.html")

def orders(request):
    '''浏览会员订单'''
    return render(request,"mobile/member_orders.html")

def detail(request):
    '''浏览会员订单详情'''
    return render(request,"mobile/member_detail.html")

def logout(request):
    '''执行会员退出'''
    return render(request,"mobile/register.html")