from django.conf.urls import url
from . import views

# 添加路由和视图函数的映射关系
urlpatterns = [
    url(r'viewdemo/',views.Index.as_view())  # 类视图
    # url(r'viewdemo/',views.my_decorator(views.Index.as_view()))  # 类视图使用装饰器---as_view()返回的是一个处理函数
]