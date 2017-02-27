# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'home.html')

def add1(request):
    a = request.GET.get('a',0)  #a = request.GET['a'] 当没有传递 a 的时候默认 a 为 0
    b = request.GET.get('b',0)
    c = int(a) + int(b)
    return HttpResponse('add1:'+str(a)+' + '+str(b)+' = '+str(c))


def add2(request,a,b):
   # a = request.GET.get('a',0)  #a = request.GET['a'] 当没有传递 a 的时候默认 a 为 0
   # b = request.GET.get('b',0)
    c = int(a) + int(b)
    return HttpResponse('add2:'+str(a)+' + '+str(b)+' = '+str(c))
