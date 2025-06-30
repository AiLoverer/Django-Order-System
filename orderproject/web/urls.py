"""
URL configuration for orderproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from web.views import index, cart, orders
from django.urls import include, path

urlpatterns = [
    path('', index.index, name="index"), #前台大堂点餐首页

    # 前台管理员路由
    path('login', index.login, name="web_login"),
    path('dologin', index.dologin, name="web_dologin"),
    path('logout', index.logout, name="web_logout"),
    path('verify', index.verify, name="web_verify"), #验证码

    path('web/',include([
        path('', index.webIndex, name="web_index"), #前台大堂点餐首页

        path('cart/add/<str:pid>', cart.add, name="web_cart_add"), #添加购物车
        path('cart/delete/<str:pid>', cart.delete, name="web_cart_delete"), #删除购物车
        path('cart/clear', cart.clear, name="web_cart_clear"), #清空购物车
        path('cart/change', cart.change, name="web_cart_change"), #修改购物车

        # 订单处理
        path('orders/<int:pIndex>', orders.index, name="web_orders_index"), #浏览订单
        path('orders/insert', orders.insert, name='web_orders_insert'), #执行订单添加操作
        path('orders/detail', orders.detail,name='web_orders_detail'), #订单的详情信息
        path('orders/status', orders.status,name='web_orders_status'), #修改订单状态

    ]))
]
