from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.urls import reverse


def index(request):
    """
    视图函数
    :param request:传入request对象
    :return:响应对象
    """
    url=reverse('users:say')  # 返回具体路由

    print(url,request.path)

    return HttpResponse('<h1>hello django</h1>')


def say(request):

    return HttpResponse('<h1>say</h1>')


def sayhello(request):
    return HttpResponse('<h1>sayhello</h1>')