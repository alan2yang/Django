from urllib import request

from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class IndexView(View):
    def get(self,request):
        return render(request,'index.html',{'city':'北京'})