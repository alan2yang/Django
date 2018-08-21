from django.conf.urls import url

from . import views

urlpatterns=[
    # url(r'weather/([a-z]+)/(\d{4})',views.weather)  # 正则匹配
    url(r'weather/(?P<city>[a-z]+)/(?P<year>\d{4})',views.weather),  # 正则匹配，分组起别名
    url(r'session_demo/',views.session_demo),
]