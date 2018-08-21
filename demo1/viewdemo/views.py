from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

# Create your views here.
from django.views.generic import View


# 定义一个装饰器---在路由上使用
def my_decorator(view_func):
    def wrapper(*args,**kwargs):
        print('调用了装饰器')
        return view_func(*args,**kwargs)
    return wrapper


class Index(View):

    @method_decorator(my_decorator)  # 调用装饰器
    def get(self,request):  # 响应get请求

        return HttpResponse('get page')

    def post(self, request):  # 响应post请求
        return HttpResponse('post page')