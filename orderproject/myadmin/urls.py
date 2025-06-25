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
from myadmin.views import index,user
from django.urls import path

urlpatterns = [
    path('', index.index, name='myadmin_index'),

    # 后台管理员路由
    path('login', index.login, name="myadmin_login"), #加载登录页面
    path('dologin', index.dologin, name="myadmin_dologin"), #执行登录操作
    path('logout', index.logout, name="myadmin_logout"), #执行退出操作
    path('verify', index.verify, name="myadmin_verify"), #验证码

    #员工账号信息管理
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),#浏览信息
    path('user/add', user.add, name="myadmin_user_add"),             #加载添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),     #执行信息添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"),#删除信息
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),#准备信息编辑
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),#执行信息编辑
]
