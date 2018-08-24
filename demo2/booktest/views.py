from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .forms import BookForm


class IndexView(View):
    def get(self,request):
        context={
            'city': '北京',
            'alist':[1,2,3],
            'adict':{
                'name':'西游记',
                'author':'吴承恩'
            }
        }
        return render(request,'index.html',context)


class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,'index.html',{'form':form})

    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('ok')

        else:
            return render(request,'index.html',{'form':form})

