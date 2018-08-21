import json

from django.http import HttpResponse

# Create your views here.


# weather/city/year/?a=1&b=2&a=3
def weather(request,year,city):
    # 获取路径参数
    # print(city)
    # print(year)

    # 获取查询参数/GET
    a=request.GET.get('a')  # 多值参数，获取最后一个
    b=request.GET.get('b')
    alist=request.GET.getlist('a')  # 获取多个值保存在列表中

    # print(a)
    # print(b)
    # print(alist)

    # 获取form表单数据/POST
    c=request.POST.get('c')  # 多值参数，获取最后一个
    d=request.POST.get('d')
    clist=request.POST.getlist('c')

    print(c)
    print(d)
    print(clist)

    print(request.body)

    # 获取非表单数据/json数据
    json_bytes=request.body
    json_str=json_bytes.decode()
    json_dict=json.loads(json_str)  # python3.6之前，只能接收str类型，之后可接收str,bytes
    #
    # print(json_dict)
    # c=json_dict.get('c')
    # d=json_dict.get('d')
    # print(c)
    # print(d)
    print(request.META['CONTENT_TYPE'])  # 获取请求头中的信息
    print(request.method)  # 获取请求方式

    return HttpResponse('OK')


def session_demo(request):
    request.session['user_id']=123
    request.session['user_name']='python'

    return HttpResponse('OK')