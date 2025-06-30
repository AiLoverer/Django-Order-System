from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from datetime import datetime

from myadmin.models import User,Shop,Category,Product,Orders,OrderDetail,Payment

def index(request,pIndex=1):
    '''浏览订单信息'''
    pass

def insert(request):
    '''大堂执行订单添加操作'''
    try:
        # 执行订单信息添加操作
        od = Orders()
        od.shop_id = request.session['shopinfo']['id'] #店铺id号
        od.member_id = 0 #会员id
        od.user_id = request.session['webuser']['id'] #操作员id
        od.money = request.session['total_money']
        od.status = 1 #订单状态:1过行中/2无效/3已完成
        od.payment_status = 2 #支付状态:1未支付/2已支付/3已退款
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()

        # 执行支付信息添加
        op = Payment()
        op.order_id = od.id #订单id号
        op.member_id = 0 #会员id号
        op.money = request.session['total_money'] #支付款
        op.type = 2 #付款方式：1会员付款/2收银收款
        op.bank = request.GET.get("bank",3) #收款银行渠道:1微信/2余额/3现金/4支付宝
        op.status = 2 #支付状态:1未支付/2已支付/3已退款
        op.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        # 执行订单详情添加
        cartlist = request.session.get('cartlist',{})
        for shop in cartlist.values():
            ov = OrderDetail()
            ov.order_id = od.id
            ov.product_id = shop['id']
            ov.product_name = shop['name']
            ov.price = shop['price']
            ov.quantity = shop['num']
            ov.status = 1
            ov.save()
        del request.session['cartlist']  
        del request.session['total_money']
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        context = {"info":"订单添加失败，请稍后再试！"}
        return HttpResponse("N")

def detail(request):
    '''加载订单信息'''
    pass

def status(request):
    ''' 修改订单状态 '''
    pass