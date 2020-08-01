from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse("第一次使用git推送代码")

def login(request):
    return redirect('/index')
