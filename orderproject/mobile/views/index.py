from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
# Create your views here.
from myadmin.models import Member

def index(request):
    ''' 移动端首页 '''
    return render(request,"mobile/index.html")

def register(request):
    ''' 移动端会员注册/登录表单 '''
    return render(request,"mobile/register.html")

def doRegister(request):
    ''' 执行会员注册/登录 '''
    #模拟短信验证
    verifycode = "1234" #reuqest.session['verifycode']
    if verifycode != request.POST['code']:
        context = {"info":'短信验证码错误'}
        return render(request,"mobile/register.html",context)

    try:
        #根据手机号码获取当前会员信息
        member = Member.objects.get(mobile=request.POST['mobile'])
    except Exception as err:
        #print(err)
        #此处可以执行当前会员注册（添加）
        ob = Member()
        ob.nickname = "顾客" #默认会员名称
        ob.avatar = "moren.png" #默认头像
        ob.mobile = request.POST['mobile'] #手机号码
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        member = ob
    #检验当前会员状态
    if member.status == 1:
        #将当前会员信息转成字典格式并存放到session中
        request.session['mobileuser'] = member.toDict()
        #重定向到登录页
        return redirect(reverse("mobile_index")) 
    else:
        context = {"info":'此账户信息禁用！'}
        return render(request,"mobile/register.html",context)


def shop(request):
    ''' 移动端选择店铺页面 '''
    return render(request,"mobile/shop.html")

def selectShop(request):
    ''' 移动端首页 '''
    #return render(request,"mobile/index.html")
    pass

def addOrders(request):
    ''' 移动端下单表单页'''
    return render(request,"mobile/addOrders.html")