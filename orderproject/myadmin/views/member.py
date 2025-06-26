#会员信息视图文件
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q

from myadmin.models import Member
import time
import os


# ==============后台会员信息管理======================
# 浏览会员信息
def index(request,pIndex=1):
    mod = Member.objects

    mlist = mod.filter(status__lt=9)
    mywhere=[]
    #获取并判断搜索条件
    kw = request.GET.get("keyword",None)
    print(kw)
    if kw:
        mlist = mlist.filter(Q(nickname__contains=kw) | Q(mobile__contains=kw))
        mywhere.append('keyword='+kw)

    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(mlist,5) #以5条每页创建分页对象
    maxpages = page.num_pages #最大页数
    #判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #当前页数据
    plist = page.page_range   #页码数列表

    #封装信息加载模板输出
    context = {"memberlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myadmin/member/index.html",context)

def edit(request,mid=0):
    '''加载信息编辑表单'''
    try:
        ob = Member.objects.get(id=mid)
        context = {'member':ob}
        print(ob.nickname)
        print(ob.mobile)
        print(ob.avatar)
        return render(request,"myadmin/member/edit.html",context)
    except Exception as err:
        print(err)
        context = {'info':"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def update(request,mid):
    pass
    '''执行信息编辑'''
    try:
        #获取原图片
        oldpicname = request.POST['oldpicname']
        print(oldpicname)
        #图片的上传处理
        myfile = request.FILES.get("avatar",None)
        if not myfile:
            avatar = oldpicname
        else:
            avatar = str(time.time())+"."+myfile.name.split('.').pop()
            destination = open("./static/uploads/member/"+avatar,"wb+")
            for chunk in myfile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()

        ob = Member.objects.get(id=mid)
        ob.nickname = request.POST['nickname']
        ob.mobile = request.POST['mobile']
        ob.avatar = avatar
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"修改成功！"}

        #判断并删除老图片
        #if myfile:
            #os.remove("./static/uploads/member/"+oldpicname)

    except Exception as err:
        print(err)
        context = {'info':"修改失败！"}
         #判断并删除新图片
        if myfile:
            os.remove("./static/uploads/member/"+avatar)
    return render(request,"myadmin/info.html",context)

def delete(request,mid=0):
    '''执行信息删除'''
    try:
        ob = Member.objects.get(id=mid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"删除成功！"}
    except Exception as err:
        print(err)
        context = {'info':"删除失败！"}
    return render(request,"myadmin/info.html",context)

def resetpwd(request,mid=0):
    '''重置密码'''
    try:
        ob = Member.objects.get(id=mid)

        #获取密码并md5
        import hashlib
        import random
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = "123456" + str(n) 
        md5.update(s.encode('utf-8'))
        ob.password_hash = md5.hexdigest()
        ob.password_salt = n
        ob.status = 1
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"密码重置成功！"}
    except Exception as err:
        print(err)
        context = {'info':"密码重置失败！"}
    return render(request,"myadmin/info.html",context)