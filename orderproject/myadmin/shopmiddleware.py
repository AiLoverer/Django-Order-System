#自定义中间类（执行是否登录判断）
from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("ShopMiddleware")

    def __call__(self, request):
        path = request.path
        print("url:",path)

        #判断管理后台是否登录
        #定义后台不登录也可直接访问的url列表
        urllist = ['/myadmin/login','/myadmin/logout','/myadmin/dologin','/myadmin/verify']
        #判断当前请求url地址是否是以/myadmin开头,并且不在urllist中，才做是否登录判断
        if re.match(r'^/myadmin',path) and (path not in urllist):
            #判断是否登录(在于session中没有adminuser)
            if 'adminuser' not in request.session:
                #重定向到登录页
                return redirect(reverse("myadmin_login"))
                #pass

        #判断大堂点餐请求的判断，判断是否登录（session中是否有webuser）
        if re.match(r'^/web',path):
            #判断是否登录(在于session中没有webuser)
            if 'webuser' not in request.session:
                #重定向到登录页
                return redirect(reverse("web_login"))

        # 移动端请求路由判断
        # 定义网站移动端不用登录也可访问的路由url
        urllist = ['/mobile/register','/mobile/doregister']
        # 判断当前请求是否是请求移动端,并且path不在urllist中
        if re.match(r"^/mobile",path) and (path not in urllist):
            # 判断当前用户是否没有登录移动端
            if "mobileuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('mobile_register'))
        
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response