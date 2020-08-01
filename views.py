from django.http import HttpResponse

def index(request):
    return HttpResponse("第一次使用git推送代码")
