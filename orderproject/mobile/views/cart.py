from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from myadmin.models import Product

# 购物车信息管理
def add(request):
    '''添加购物车'''
    print('----------------------------add cart')
    cartlist = request.session.get("mobile_cartlist",{})
    pid = request.GET.get("pid",None)
    print(pid)
    if pid is not None:
        product = Product.objects.get(id=pid).toDict()
        product['num'] = 1

        #判断购物车中是否已存在要购买的商品
        if pid in cartlist:
            cartlist[pid]['num'] += product['num'] #累加购买量
        else:
            cartlist[pid] = product
        #将购物车中的商品信息放回到session中
        request.session['mobile_cartlist'] = cartlist
        print(cartlist)
    #响应json格式的购物车信息
    return JsonResponse({'cartlist':cartlist})

def delete(request,pid):
    '''删除购物车中的商品'''
    cartlist = request.session['mobile_cartlist']
    del cartlist[pid]
    request.session['mobile_cartlist'] = cartlist
    #响应json格式的购物车信息
    return JsonResponse({'cartlist':cartlist})

def clear(request):
    '''清空购物车'''
    request.session['mobile_cartlist'] = {}
    #响应json格式的购物车信息
    return JsonResponse({'cartlist':{}})

def change(request):
    '''购物车信息修改'''
    cartlist = request.session['mobile_cartlist']
    shopid = request.GET.get("pid",0)
    num = int(request.GET.get('num',1))

    print(shopid,num)
    if num < 1:
        num = 1
    cartlist[shopid]['num'] = num
    request.session['mobile_cartlist'] = cartlist
    #响应json格式的购物车信息
    return JsonResponse({'cartlist':cartlist})

