from django.conf.urls import url
from . import views

# 添加路由和视图函数的映射关系
urlpatterns = [
    url(r'^index/',views.index),
    url(r'^say/',views.say,name='say'),  # name 路由名称
    url(r'^sayhello/',views.sayhello,name='sayhello'),
]
