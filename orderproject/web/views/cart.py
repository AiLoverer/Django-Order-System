from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

# 购物车页面操作
def add(request, pid=0): 
    '''添加商品'''
    #从session中的菜品列表productlist中获取要添加购物车中的菜品信息
    product = request.session['productlist'][pid]
    #追加一个购买数量，默认为1
    product['num'] = 1
    #从session中获取购物车cartlist信息，若没有默认为空字典{}
    cartlist = request.session.get('cartlist', {})
    #判断购物车中是否已经存在该商品，若存在则数量+1，若不存在则添加到购物车中
    if pid in cartlist:
        cartlist[pid]['num'] += 1
    else:
        cartlist[pid] = product
    #将购物车信息更新到session中
    print(cartlist)
    request.session['cartlist'] = cartlist
    #返回购物车页面
    return redirect(reverse('web_index'))

def delete(request, pid=0): 
    '''删除商品'''
    #从session中获取购物车cartlist信息，若没有默认为空字典{}
    cartlist = request.session.get('cartlist', {})
    #判断购物车中是否存在该商品，若存在则删除，若不存在则什么也不做 
    if pid in cartlist:
        del cartlist[pid]
    #将购物车信息更新到session中
    request.session['cartlist'] = cartlist
    #返回购物车页面
    return redirect(reverse('web_index'))
    pass

def clear(request): 
    '''清空购物车'''
    #从session中删除购物车信息
    del request.session['cartlist']
    #返回购物车页面
    return redirect(reverse('web_index'))
    pass

def change(request): 
    '''修改购物车'''
    #从session中获取购物车cartlist信息，若没有默认为空字典{}
    cartlist = request.session.get('cartlist', {})
    #获取修改的商品id和数量
    pid = request.GET.get('pid', 0)
    num = int(request.GET.get('num', 1))
    print("----:"+str(pid))
    print("----:"+str(num))
    if num < 1:
        num = 1
    #判断购物车中是否存在该商品，若存在则修改数量，若不存在则什么也不做 
    if pid in cartlist:
        cartlist[pid]['num'] = num
    #将购物车信息更新到session中
    request.session['cartlist'] = cartlist
    #返回购物车页面
    return redirect(reverse('web_index'))